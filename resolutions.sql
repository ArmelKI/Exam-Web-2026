CREATE TABLE resolutions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pseudo TEXT NOT NULL,
    texte TEXT NOT NULL,
    votes INTEGER NOT NULL CHECK (votes>=0) DEFAULT 0,
    statut TEXT CHECK (statut IN ('active', 'kept', 'dropped')) DEFAULT 'active',
    created_at DATETIME DEFAULT CURRENT_DATE
);

INSERT INTO resolutions (pseudo, texte, votes, statut, created_at) VALUES ('G.O.', 'Rendre ses notes rapidement', 3, 'active', '2025-01-05');
INSERT INTO resolutions (pseudo, texte, votes, statut, created_at) VALUES ('Pierre L.', 'Faire des examens plus faciles', 6, 'dropped', '2025-01-02');
INSERT INTO resolutions (pseudo, texte, votes, statut, created_at) VALUES ('Mr. Bou', 'Rire en silence', 1, 'kept', '2025-01-03');