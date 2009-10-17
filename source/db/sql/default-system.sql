;-- System Registry
CREATE TABLE systemregistry(
	"key" VARCHAR(50) PRIMARY KEY NOT NULL,
	"value" VARCHAR(50) DEFAULT NULL,
	"module" VARCHAR(50)  DEFAULT NULL
);

;-- System information table
CREATE TABLE systeminformation(
	"key" VARCHAR(50) PRIMARY KEY NOT NULL,
	"value" VARCHAR(50) DEFAULT NULL
);

;-- Main project table
CREATE TABLE projects(
    "id" INTEGER PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "datecreated" DATETIME DEFAULT current_timestamp
);

;-- Associated project files
CREATE TABLE projectincludes(
    "id" INTEGER,
    "projectid" INTEGER NOT NULL,
    "path" VARCHAR(255) NOT NULL,
    PRIMARY KEY ("id")
);


;-- DEFAULT EDITOR VALUES
INSERT INTO systemregistry(key,value,module) VALUES ('fontface','Verdana','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('fontsize','12','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('textmargin','200','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('tabsize','4','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('usetab','1','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('foldcode','1','editor');
INSERT INTO systemregistry(key,value,module) VALUES ('foldcodestyle','1','editor');