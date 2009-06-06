-- System Registry
CREATE TABLE systemregistry(
	"key" VARCHAR(50) PRIMARY KEY NOT NULL,
	"value" VARCHAR(50) DEFAULT NULL,
	"module" VARCHAR(50)  DEFAULT NULL
);

-- System information table
CREATE TABLE systeminformation(
	"key" VARCHAR(50) PRIMARY KEY NOT NULL,
	"value" VARCHAR(50) DEFAULT NULL
);