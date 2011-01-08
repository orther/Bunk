\set ON_ERROR_STOP 1;

-- ============================================================================
-- PUBLIC SCHEMA
-- ============================================================================

DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;

SET search_path TO public;

-- ============================================================================
-- TABLES
-- ============================================================================

CREATE TABLE "user" (

    -- ids
    user_id BIGSERIAL NOT NULL PRIMARY KEY,

    -- details
    email         VARCHAR(65),
    password_hash VARCHAR(32) NOT NULL,
    username      VARCHAR(50) NOT NULL UNIQUE,

    -- statuses
    is_deleted BOOLEAN NOT NULL DEFAULT false,

    -- dates
    date_created     TIMESTAMP NOT NULL DEFAULT NOW(),
    date_modified    TIMESTAMP,
    date_last_log_in TIMESTAMP

);
