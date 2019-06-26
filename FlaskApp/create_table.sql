PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE temps(
	name DEFAULT 'RPi.dev',
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	time DATETIME DEFAULT (datetime('now','localtime')),
	temperature NUMERIC NOT NULL
);

COMMIT;
