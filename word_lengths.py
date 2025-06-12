import matplotlib.pyplot as plt

english_text = "In molecular biology, a transcription factor (TF) (or sequence-specific DNA-binding factor) is a protein that controls the rate of transcription of genetic information from DNA to messenger RNA, by binding to a specific DNA sequence.[1][2] The function of TFs is to regulate—turn on and off—genes in order to make sure that they are expressed in the desired cells at the right time and in the right amount throughout the life of the cell and the organism. Groups of TFs function in a coordinated fashion to direct cell division, cell growth, and cell death throughout life; cell migration and organization (body plan) during embryonic development; and intermittently in response to signals from outside the cell, such as a hormone. There are approximately 1600 TFs in the human genome.[3][4][5] Transcription factors are members of the proteome as well as regulome. TFs work alone or with other proteins in a complex, by promoting (as an activator), or blocking (as a repressor) the recruitment of RNA polymerase (the enzyme that performs the transcription of genetic information from DNA to RNA) to specific genes.[6][7][8]. A defining feature of TFs is that they contain at least one DNA-binding domain (DBD), which attaches to a specific sequence of DNA adjacent to the genes that they regulate.[9][10] TFs are grouped into classes based on their DBDs.[11][12] Other proteins such as coactivators, chromatin remodelers, histone acetyltransferases, histone deacetylases, kinases, and methylases are also essential to gene regulation, but lack DNA-binding domains, and therefore are not TFs. TFs are of interest in medicine because TF mutations can cause specific diseases, and medications can be potentially targeted toward them."
german_text = "In der Molekularbiologie ist ein Transkriptionsfaktor (TF) (oder sequencespezifischer DNA-bindender Faktor) ein Protein, das die Rate der Transkription genetischer Informationen von DNA zu mRNA steuert, indem es sich an eine spezifische DNA-Sequenz bindet. Die Funktion von TFs besteht darin, die Gene zu regulieren – sie ein- und auszuschalten –, um sicherzustellen, dass sie in den gewünschten Zellen zur richtigen Zeit und in der richtigen Menge im Laufe des Lebens der Zelle und des Organismus exprimiert werden. Gruppen von TFs arbeiten koordiniert, um Zellteilung, Zellwachstum und Zelltod während des gesamten Lebens zu orchestrieren; Zellmigration und -organisation (Körperplan) während der embryonalen Entwicklung; und intermittierend als Antwort auf Signale von außerhalb der Zelle, wie ein Hormon. Im menschlichen Genom gibt es ungefähr 1600 TFs. Transkriptionsfaktoren sind sowohl Mitglieder des Proteoms als auch des Reguloms. TFs funktionieren alleine oder mit anderen Proteinen in einem Komplex, indem sie die Rekrutierung der RNA-Polymerase (das Enzym, das die Transkription genetischer Informationen von DNA zu RNA durchführt) zu spezifischen Genen fördern (als Aktivator) oder blockieren (als Repressor). Ein charakteristisches Merkmal von TFs ist, dass sie mindestens eine DNA-bindende Domäne (DBD) enthalten, die an eine spezifische DNA-Sequenz in der Nähe der Gene bindet, die sie regulieren. TFs werden basierend auf ihren DBDs in Klassen gruppiert. Andere Proteine wie Coaktivatoren, Chromatin-Remodelers, Histonacetyltransferasen, Histondeacetylasen, Kinasen und Methylasen sind ebenfalls wichtig für die Genregulation, aber sie besitzen keine DNA-bindenden Domänen und sind daher keine TFs. TFs sind in der Medizin von Interesse, weil TF-Mutationen spezifische Krankheiten verursachen können und Medikamente potenziell auf sie abzielen können."

english_words = []
german_words = []

word_length = 0
for i in range(0, len(english_text)):
 
    if english_text[i] != " ":
        word_length += 1
    else:
        english_words.append(word_length)
        word_length = 0

word_length = 0
for i in range(0, len(german_text)):

    if german_text[i] != " ":
        word_length += 1
    else:
        german_words.append(word_length)
        word_length = 0  

plt.plot(english_words, 'p')
plt.plot(german_words, 'p')
plt.show()

