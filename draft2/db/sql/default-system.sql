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

-- DEFAULT EDITOR VALUES
INSERT INTO systemregistry(key,value,module) VALUES ('fontface','Verdana','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('fontsize','12','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('textmargin','200','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('tabsize','4','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('usetab','1','editor');