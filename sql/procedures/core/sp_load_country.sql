CREATE OR ALTER PROCEDURE [core].[sp_load_country]
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON

    DECLARE @merge_stats TABLE
                         (
                             action_type VARCHAR(10)
                         )

    BEGIN TRY

        BEGIN TRANSACTION;
            WITH source_data AS (
                SELECT S.system_id,
                       S.system_created_at,
                       S.system_modified_at,
                       S.code,
                       S.name

                FROM staging.country as S

                )
                MERGE INTO core.country as T
            USING source_data as S
            ON (T.system_id = S.system_id)

            WHEN MATCHED AND S.system_modified_at > T.system_modified_at
                THEN
                UPDATE
                SET T.system_modified_at = S.system_modified_at,
                    T.code               = S.code,
                    T.name               = S.name

            WHEN NOT MATCHED BY TARGET THEN

                INSERT (code, name, system_id, system_created_at, system_modified_at)
                VALUES (S.code, S.name, S.system_id, S.system_created_at, S.system_modified_at)
                OUTPUT $action INTO @merge_stats;

        COMMIT TRANSACTION;

        SELECT ISNULL(SUM(IIF(action_type = 'INSERT', 1, 0)), 0) AS rows_inserted,
               ISNULL(SUM(IIF(action_type = 'UPDATE', 1, 0)), 0) AS rows_updated

        FROM @merge_stats

    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION

        THROW


    END CATCH
END;
GO


