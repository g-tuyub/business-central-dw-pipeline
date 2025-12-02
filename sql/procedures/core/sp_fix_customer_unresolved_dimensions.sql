CREATE OR ALTER PROCEDURE [core].[fix_customer_unresolved_dimensions]
AS
BEGIN
    /*
     * ======================================================================================
     * PROCESO: reparar 'late arriving dimensions' en core.customer
     * ======================================================================================
     * Objetivo:
     * Buscamos todas las filas en la tabla [core].[customer] que tienen -1 en surrogate keys hacia otras dimensiones
     * Luego Buscamos el valor real, asumiendo que ya se ha cargado, en la tabla de la dimension correspondiente, haciendo JOIN por medio de natural keys
     * * LOGICA:
     * 1. LEFT JOIN tabla customer a todas sus dimensiones relacionadas por medio de natural keys.
     * 2. Usamos IIF + COALESCE para que, si encontró una coincidencia, actualiza la columna, si no, mantiene -1.
     * 3. Optimización en la condición WHERE, para actualizar filas solo en donde existe al menos un -1 para alguna de las columnas.
     * * DEVUELVE:
     * row_count que indica cuantas filas se 'repararon'.
     * ======================================================================================
     */

    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    DECLARE @rows_affected INT = 0;

    BEGIN TRY
        BEGIN TRANSACTION;

            UPDATE c
            SET
                -- Lógica: si es -1, busca el id correspondiente. Si no lo encuentras, mantén -1. Si el valor ya era válido, mantén ese valor.
                c.customer_posting_group_id = IIF(c.customer_posting_group_id = -1, COALESCE(cpg.id, -1), c.customer_posting_group_id),
                c.customer_price_group_id   = IIF(c.customer_price_group_id = -1,   COALESCE(cprg.id, -1), c.customer_price_group_id),
                c.currency_id               = IIF(c.currency_id = -1,               COALESCE(cu.id, -1),   c.currency_id),
                c.payment_term_id           = IIF(c.payment_term_id = -1,           COALESCE(pt.id, -1),   c.payment_term_id),
                c.payment_method_id         = IIF(c.payment_method_id = -1,         COALESCE(pm.id, -1),   c.payment_method_id),
                c.salesperson_id            = IIF(c.salesperson_id = -1,            COALESCE(s.id, -1),    c.salesperson_id),
                c.shipment_method_id        = IIF(c.shipment_method_id = -1,        COALESCE(sm.id, -1),   c.shipment_method_id),
                c.location_id               = IIF(c.location_id = -1,               COALESCE(l.id, -1),    c.location_id),
                c.country_id                = IIF(c.country_id = -1,                COALESCE(co.id, -1),   c.country_id)

            FROM [core].[customer] AS c
            LEFT JOIN [core].[customer_posting_group] AS cpg  ON c.customer_posting_group_code = cpg.code
            LEFT JOIN [core].[customer_price_group]   AS cprg ON c.customer_price_group_code = cprg.code
            LEFT JOIN [core].[currency]               AS cu   ON c.currency_code = cu.code
            LEFT JOIN [core].[payment_term]           AS pt   ON c.payment_term_code = pt.code
            LEFT JOIN [core].[payment_method]         AS pm   ON c.payment_method_code = pm.code
            LEFT JOIN [core].[salesperson]            AS s    ON c.salesperson_code = s.code
            LEFT JOIN [core].[shipment_method]        AS sm   ON c.shipment_method_code = sm.code
            LEFT JOIN [core].[location]               AS l    ON c.location_code = l.code
            LEFT JOIN [core].[country]                AS co   ON c.country_code = co.code

            WHERE
                -- OPTIMIZACION: sólo realiza operación de escritura en las filas que tienen al menos una incidencia (-1),
                -- y además encontró al menos una solución.
                -- (NOTA: si te parece raro, piénsalo así:
                -- esto tiene sentido, debido a que teóricamente puede encontrar filas con varios -1, pero al hacer los JOINS, no encontrar ninguna solución.
                -- en ese caso si no somos estrictos con el filtro (JOIN IS NOT NULL), sobreescribe los mismos valores,
               -- aquí somos eficientes al evitar sobreescribir si ese es el caso).

                (c.customer_posting_group_id = -1 AND cpg.id IS NOT NULL)
                OR (c.customer_price_group_id = -1 AND cprg.id IS NOT NULL)
                OR (c.currency_id = -1             AND cu.id IS NOT NULL)
                OR (c.payment_term_id = -1         AND pt.id IS NOT NULL)
                OR (c.payment_method_id = -1       AND pm.id IS NOT NULL)
                OR (c.salesperson_id = -1          AND s.id IS NOT NULL)
                OR (c.shipment_method_id = -1      AND sm.id IS NOT NULL)
                OR (c.location_id = -1             AND l.id IS NOT NULL)
                OR (c.country_id = -1              AND co.id IS NOT NULL);

            -- Capturamos el conteo de filas afectadas
            SET @rows_affected = @@ROWCOUNT;

        COMMIT TRANSACTION;

        -- Devuelve el número de filas afectadas
        SELECT @rows_affected AS [RowsFixed];

    END TRY
    BEGIN CATCH
        -- Si algo sale mal, rollback
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        THROW;
    END CATCH
END;
GO
