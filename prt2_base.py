import json
class Model:
    title = input("Введите заголовок: ")
    text = input("Введите текст сообщения: ")
    author = input("Введите автора сообщения: ")
    def _save(self):
        with open(f"model_attributes_{self.author}.json", "w", encoding="utf-8") as file:
            list_atr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
            list_atr = list_atr[::-1]
            list_value = []
            for i in list_atr:
                value = getattr(Model, f"{i}")
                list_value.append(value)
            data = dict(zip(list_atr, list_value))
            json.dump(data, file, ensure_ascii=False)
            print("Data save!")

state = Model()
state._save()