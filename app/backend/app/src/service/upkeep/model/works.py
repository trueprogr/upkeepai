import pandas as pd

data = {
    "№\nп/п": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "Код": [105, 26, 9, 104, 20, 3, 5, 4, 4, 53, 52, 51, 1, 2, 9, 3, 5, 4, 11, 4, 8, 12, 13, 10, 333, 28, 106, 321, 6],
    "Наименование": ["строительный контроль", "ремонт подъездов, направленный на восстановление их надлежащего состояния и проводимый при выполнении иных работ", "ремонт фасада (замена оконных блоков, расположенных в помещениях общего пользования в многоквартирном доме)", "проведение экспертизы проектной документации по объектам культурного наследия федерального значения", "разработка проектной документации", "ремонт внутридомовых инженерных систем теплоснабжения (разводящие магистрали)", "ремонт внутридомовых инженерных систем водоотведения (канализации) (выпуски и сборные трубопроводы)", "ремонт внутридомовых инженерных систем горячего водоснабжения (разводящие магистрали)", "ремонт внутридомовых инженерных систем холодного водоснабжения (разводящие магистрали)", "ремонт или замена мусоропровода", "ремонт пожарного водопровода", "ремонт внутридомовой системы дымоудаления и противопожарной автоматики", "ремонт внутридомовых инженерных сетей электроснабжения", "ремонт внутридомовых инженерных систем газоснабжения", "ремонт подвальных помещений, относящихся к общему имуществу собственников помещений", "ремонт внутридомовых инженерных систем теплоснабжения (стояки)", "ремонт внутридомовых инженерных систем водоотведения (канализации) (стояки)", "ремонт внутридомовых инженерных систем горячего водоснабжения (стояки)", "ремонт фундамента", "ремонт внутридомовых инженерных систем холодного водоснабжения (стояки)", "ремонт крыши", "ремонт или замена внутреннего водостока", "ремонт балконов", "ремонт фасада", "оценка соответствия лифтов", "Разработка и проведение экспертизы ПД, в том числе АН за проведением работ по сохранению ОКН, выявленных ОКН, научное руководство проведением указанных работ в случае проведения работ по КР ОИ в МКД  г. Москвы, являющихся ОКН, выявленными ОКН.", "Авторский надзор", "разработка проектной документации по лифтам", "замена лифтового оборудования"],
    "Наименование объекта общего имущества": ["Строительный контроль", "Подъезд", "Фасад(оконные блоки)", "проведение экспертизы", "разработка проектной документации", "Внутридомовые системы отопления (магистрали)", "Внутридомовые системы канализации (магистрали)", "Внутридомовые инженерные системы горячего водоснабжения (магистрали)", "Внутридомовые системы холодного водоснабжения (магистрали)", "Мусоропровод", "Пожарный водопровод", "Системы дымоудаления", "Внутридомовые системы электроснабжения", "Внутридомовые инженерные системы газоснабжения", "Подвальные помещения, относящиеся к общему имуществу", "Внутридомовые системы отопления (стояки)", "Внутридомовые системы канализации (стояки)", "Внутридомовые инженерные системы горячего водоснабжения (стояки)", "Фундамент", "Внутридомовые системы холодного водоснабжения (стояки)", "Крыша", "Внутренний водосток", "Фасад (балконы)", "Фасад", "оценка соответствия лифтов", "Разработка и проведение экспертизы ПД, в том числе АН за проведением работ по сохранению ОКН, выявленных ОКН, научное руководство проведением указанных работ в случае проведения работ по КР ОИ в МКД  г. Москвы, являющихся ОКН, выявленными ОКН.", "Авторский надзор", "разработка проектной документации по лифтам", "Лифт"],
    "Тип работ": ["Услуга", "Работа", "Работа", "Услуга", "Услуга", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Работа", "Услуга", "Работа", "Услуга", "Услуга", "Работа"],
    "Группа работ": ["Стройконтроль", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "СМР", "Оценка соответствия лифтов", "Не задано", "Не задано", "Лифты", "Лифты"],
    "Сокращенное наименование работы": ["СК", "Подъезд", "Окна", "проведение экспертизы", "ПСД", "ЦО-М", "КАН-М", "ГВС-М", "ХВС-М", "Мусоропровод", "ПВ", "ППАиДУ", "ЭС", "ГАЗ", "Подвал", "ЦО", "КАН", "ГВС", "Фундамент", "ХВС", "Крыша", "ВДСК", "Балкон", "Фасад", "Оценка", "Разработка и проведение экспертизы ПД, в том числе АН за проведением работ по сохранению ОКН, выявленных ОКН, научное руководство проведением указанных работ в случае проведения работ по КР ОИ в МКД  г. Москвы, являющихся ОКН, выявленными ОКН.", "Авторский надзор", "ПСД лифты", "Лифт"]
}

df_4 = pd.DataFrame(data)

