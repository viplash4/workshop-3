
CREATE TABLE city_info (
    city_name    VARCHAR2(20) NOT NULL,
    city_state   VARCHAR2(20) NOT NULL,
    stat_year    NUMBER(4) NOT NULL,
    city_gdp     NUMBER(10),
    city_rating  NUMBER(4)
);

ALTER TABLE city_info
    ADD CONSTRAINT city_info_pk PRIMARY KEY ( stat_year,
                                              city_name,
                                              city_state );
                                              
CREATE TABLE full_city_address (
    city_name          VARCHAR2(20) NOT NULL,
    city_state  VARCHAR2(20) NOT NULL
);

ALTER TABLE full_city_address ADD CONSTRAINT full_city_address_pk PRIMARY KEY ( city_name,
                                                                                city_state );
CREATE TABLE states (
    city_state VARCHAR2(20) NOT NULL
);

ALTER TABLE states ADD CONSTRAINT states_pk PRIMARY KEY ( city_state );

ALTER TABLE full_city_address
    ADD CONSTRAINT full_city_address_states_fk FOREIGN KEY ( city_state )
        REFERENCES states ( city_state );
        
ALTER TABLE city_info
    ADD CONSTRAINT city_info_fk FOREIGN KEY ( city_name,city_state )
        REFERENCES full_city_address ( city_name,city_state );
        
-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              5
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0

                                              