import human
import family
import datetime
father = human.Human("Andrey", "man", datetime.datetime.strptime("12.08.1997", "%d.%m.%Y"), [], [])
mother = human.Human("Oly", "Women", datetime.datetime.strptime("12.02.1957", "%d.%m.%Y"), [], [])
children = human.Human("Misha", "man", datetime.datetime.strptime("19.03.2005", "%d.%m.%Y"), [father, mother], [])
father.append_children(children)
mother.append_children(mother)
family_1 = family.Family([])
family_1.append_human(father)
family_1.append_human(mother)
family_1.append_human(children)
family_1.view_family()


