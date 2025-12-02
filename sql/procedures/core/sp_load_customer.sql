CREATE OR ALTER PROCEDURE [core].[sp_load_customer]
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

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
                       S.name,

                       CASE
                           WHEN S.customer_posting_group_code IS NULL THEN NULL
                           WHEN cpg.id IS NULL THEN -1
                           ELSE cpg.id
                           END AS customer_posting_group_id,
                       S.customer_posting_group_code,

                       CASE
                           WHEN S.customer_price_group_code IS NULL THEN NULL
                           WHEN cpr.id IS NULL THEN -1
                           ELSE cpr.id
                           END AS customer_price_group_id,
                       S.customer_price_group_code,

                       CASE
                           WHEN S.currency_code IS NULL THEN NULL
                           WHEN cur.id IS NULL THEN -1
                           ELSE cur.id
                           END AS currency_id,
                       S.currency_code,

                       CASE
                           WHEN S.payment_term_code IS NULL THEN NULL
                           WHEN pt.id IS NULL THEN -1
                           ELSE pt.id
                           END AS payment_term_id,
                       S.payment_term_code,

                       CASE
                           WHEN S.payment_method_code IS NULL THEN NULL
                           WHEN pm.id IS NULL THEN -1
                           ELSE pm.id
                           END AS payment_method_id,
                       S.payment_method_code,

                       CASE
                           WHEN S.salesperson_code IS NULL THEN NULL
                           WHEN sp.id IS NULL THEN -1
                           ELSE sp.id
                           END AS salesperson_id,
                       S.salesperson_code,

                       CASE
                           WHEN S.shipment_method_code IS NULL THEN NULL
                           WHEN sm.id IS NULL THEN -1
                           ELSE sm.id
                           END AS shipment_method_id,
                       S.shipment_method_code,

                       CASE
                           WHEN S.location_code IS NULL THEN NULL
                           WHEN loc.id IS NULL THEN -1
                           ELSE loc.id
                           END AS location_id,
                       S.location_code,

                       CASE
                           WHEN S.country_code IS NULL THEN NULL
                           WHEN cou.id IS NULL THEN -1
                           ELSE cou.id
                           END AS country_id,
                       S.country_code,

                       S.address_line_1,
                       S.address_line_2,
                       S.postal_code,
                       S.ship_to_address_code,
                       S.credit_limit,
                       S.combine_shipments,
                       S.dimension_1_code,
                       S.dimension_2_code,
                       S.blocked,
                       S.priority

                FROM staging.customer AS S
                         LEFT JOIN core.customer_posting_group cpg ON S.customer_posting_group_code = cpg.code
                         LEFT JOIN core.customer_price_group cpr ON S.customer_price_group_code = cpr.code
                         LEFT JOIN core.currency cur ON S.currency_code = cur.code
                         LEFT JOIN core.payment_term pt ON S.payment_term_code = pt.code
                         LEFT JOIN core.payment_method pm ON S.payment_method_code = pm.code
                         LEFT JOIN core.salesperson sp ON S.salesperson_code = sp.code
                         LEFT JOIN core.shipment_method sm ON S.shipment_method_code = sm.code
                         LEFT JOIN core.location loc ON S.location_code = loc.code
                         LEFT JOIN core.country cou ON S.country_code = cou.code
                )
                MERGE INTO core.customer AS T
            USING source_data AS S
            ON (T.system_id = S.system_id)

            WHEN MATCHED AND S.system_modified_at > T.system_modified_at
                THEN
                UPDATE
                SET T.system_modified_at          = S.system_modified_at,
                    T.code                        = S.code,
                    T.name                        = S.name,
                    T.customer_posting_group_id   = S.customer_posting_group_id,
                    T.customer_posting_group_code = S.customer_posting_group_code,
                    T.customer_price_group_id     = S.customer_price_group_id,
                    T.customer_price_group_code   = S.customer_price_group_code,
                    T.currency_id                 = S.currency_id,
                    T.currency_code               = S.currency_code,
                    T.payment_term_id             = S.payment_term_id,
                    T.payment_term_code           = S.payment_term_code,
                    T.payment_method_id           = S.payment_method_id,
                    T.payment_method_code         = S.payment_method_code,
                    T.salesperson_id              = S.salesperson_id,
                    T.salesperson_code            = S.salesperson_code,
                    T.shipment_method_id          = S.shipment_method_id,
                    T.shipment_method_code        = S.shipment_method_code,
                    T.location_id                 = S.location_id,
                    T.location_code               = S.location_code,
                    T.country_id                  = S.country_id,
                    T.country_code                = S.country_code,
                    T.address_line_1              = S.address_line_1,
                    T.address_line_2              = S.address_line_2,
                    T.postal_code                 = S.postal_code,
                    T.ship_to_address_code        = S.ship_to_address_code,
                    T.credit_limit                = S.credit_limit,
                    T.combine_shipments           = S.combine_shipments,
                    T.dimension_1_code            = S.dimension_1_code,
                    T.dimension_2_code            = S.dimension_2_code,
                    T.blocked                     = S.blocked,
                    T.priority                    = S.priority

            WHEN NOT MATCHED BY TARGET THEN
                INSERT (system_id, system_created_at, system_modified_at, code, name,
                        customer_posting_group_id, customer_posting_group_code,
                        customer_price_group_id, customer_price_group_code,
                        currency_id, currency_code,
                        payment_term_id, payment_term_code,
                        payment_method_id, payment_method_code,
                        salesperson_id, salesperson_code,
                        shipment_method_id, shipment_method_code,
                        location_id, location_code,
                        country_id, country_code,
                        address_line_1, address_line_2, postal_code, ship_to_address_code,
                        credit_limit, combine_shipments, dimension_1_code, dimension_2_code,
                        blocked, priority)
                VALUES (S.system_id, S.system_created_at, S.system_modified_at, S.code, S.name,
                        S.customer_posting_group_id, S.customer_posting_group_code,
                        S.customer_price_group_id, S.customer_price_group_code,
                        S.currency_id, S.currency_code,
                        S.payment_term_id, S.payment_term_code,
                        S.payment_method_id, S.payment_method_code,
                        S.salesperson_id, S.salesperson_code,
                        S.shipment_method_id, S.shipment_method_code,
                        S.location_id, S.location_code,
                        S.country_id, S.country_code,
                        S.address_line_1, S.address_line_2, S.postal_code, S.ship_to_address_code,
                        S.credit_limit, S.combine_shipments, S.dimension_1_code, S.dimension_2_code,
                        S.blocked, S.priority)
                OUTPUT $action into @merge_stats;

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

