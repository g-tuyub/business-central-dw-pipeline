IF NOT EXISTS (SELECT 1 FROM [core.country] WHERE  [id] = -1)

   BEGIN

        DECLARE @default_uuid UNIQUEIDENTIFIER = '00000000-0000-0000-0000-000000000000';
        DECLARE @default_datetime DATETIME2 = '1900-01-01 00:00:00';

SET IDENTITY_INSERT [core].[country] ON;

INSERT INTO [core].[country] (
                               id,
                               code,
                               name,
                               system_id,
                               system_created_at,
                               system_modified_at,
                               system_created_by_id,
                               system_modified_by_id)
VALUES (
    -1,
    '<UNKNOWN>',
    '<UNKNOWN>',
    @default_uuid,
    @default_datetime,
    @default_datetime,
    @default_uuid,
    @default_uuid
    )

SET IDENTITY_INSERT [core].[country] OFF;

    END;