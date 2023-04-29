# Start your way in Figma and go to the <a href="https://www.figma.com/file/4HbMyZxgJKBLKcD9ZaBLh8/It's_Project_NLP?type=design&node-id=0-1&t=Hb6iKImZlqch5dmd-0" target="_blank">presentation</a>
НУМЕРАЦИЯ СЛАЙДОВ СООТВЕТСВУЕТ НОМЕРУ ПУНКТА

В общем проходитесь одновременно по figma и read.me

# 1) Предобработка
* Подаем описание мероприятия и разбиваем его на всевозможные словосочетания
* <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Code/Projecting/Objects/Analysers/Functions/get_word_pairs.py">Сама функция</a>
* <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Code/Projecting/Objects/Analysers/Functions/get_word_pairs.py">Её example</a>

# 2) Векторизация
* Мы получили блок словосочетаний, для дальнейшей работы их надо векторизировать
```Python
def get_vectorized_wp_and_wp(text, vectorizer):
    list_of_wp = list()
    list_of_vectors = list()
    for sentence in text.split('.'):
        for wp in get_wp_in_line_hard(sentence):
            list_of_vectors.append(vectorizer(wp))
            list_of_wp.append(wp)
    return np.array(list_of_wp), np.array(list_of_vectors)
```
* Думаю вывод тут не рьезателен

# 3) Фильтрация
* Отфильтровываем словосочетания, которые  являются дескрипторами.
  * У нас есть нейронная сеть, которая способная предсказать, является ли словосочетание дескриптором
  * Она была обучена на основе уже готового датасета с дескрипторами
  * <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Data/data.json">Готовый датасет</a>
  * <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Code/Teach/is_descriptor_spacy.ipynb">Сама нейронка</a>
* Т.е на этом шаге мы получаем только те словосочетания, которые могут быть дескрипторами

# 4) COS distance

* Так как у нас получается множество дескрипторов(мы должны выбрать наиболее подходящий) => мы считаем косинусное расстояние от каждого к каждому
* <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Code/Projecting/Objects/Functions/get_wp_distances.py">Сама функция</a>
* БЕЗУСЛОВНО У НАС ИЗ МЕРОПРИЯТИЯ МОЖЕТ ВЫДИЛИТЬСЯ НЕСКОЛЬКО ДЕСКРИПТОРОВ(НО ПОКА МЫ ОСТАВИЛИ ТАК)

# 5) Выделение ЗУВ

* Находим вероятностную характеристику значимости дескриптора в каждомму параметру для ЗУВ
* <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Code/Teach/vectorize_from_discriptors_KCM.ipynb">Нейронная</a> сеть, которая это делает


# Дальше идёт резюме рабоыты проекта
* Его выполнение(сам main, который совмещает в себе всё выше сказанное) можно посмотреть <a href="https://github.com/MikeTsvirkunov/ITS_project/blob/FastApi/Code/Projecting/main.py">Здесь</a>






# Использованные модели

<b>nlp_type_of_event_extraction</b> $-$ pipeline для spacy.nlp достающий тип мероприятия (лекция, совещание, встреча и т.д.) из предложения.
<br>
<b>nlp_classic</b> $-$ pipeline для spacy.nlp представляющий из себя класический ru_core_news_sm pipeline.
<br>
<b>kcm_extraction_model</b> $-$ модель декодирующая вектор spacy в вектор kcm (знать, уметь, владеть)
<br>
<b>is_description_model</b> $-$ модель проверяющая является ли входной текст дескриптором или нет, возвращая степень уверенности в этом.

***
# Входные данные

json-файл состоящий из:
- id $-$ индентификатор студента;
- name_of_event $-$ названия мероприятия;
- event_description $-$ описание мероприятия;

## Пример входных данных
{<br>
$~~~~$ `"id"`: "asd",
<br>
$~~~~$ `"name_of_event"`: "Собрание по петухону",
<br>
$~~~~$`"event_description"`: "Курс является частью программы по созданию и поддержанию пространства коллективной работы «Предпринимательские Точки кипения», реализуемой в рамках федерального проекта «Платформа университетского технологического предпринимательства» при поддержке Министерства науки и высшего образования Российской Федерации и АНО «Платформа НТИ»."
}

***
# Возвращает
json-файл состоящий из:
- id $-$ индентификатор студента;
- types_of_events $-$ тип(ов) мероприятия;
- skills $-$ наименования извлечённых дескрипторов / kcm;

## Пример выходных данных
![alt text](./img.png)
