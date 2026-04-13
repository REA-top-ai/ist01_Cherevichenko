def is_alive(func):
    def wrapper(self, *args, **kwargs):
        if self.health <= 0:
            print(f'{self.name} мертв и не может действовать!')
            return None
        return func(self, *args, **kwargs)
    return wrapper


def log_action(func):
    def wrapper(self, *args, **kwargs):
        print(f'[LOG] Начало действия: {func.__name__}')
        result = func(self, *args, **kwargs)
        print('[LOG] Действие завершено')
        return result
    return wrapper


# Пасхальный бафф
def easter_buff(func):
    def wrapper(self, *args, **kwargs):
        old_health = self.health
        old_mana = self.mana

        self.health *= 2
        self.mana = int(self.mana * 1.5)

        print('Пасхальный бафф активирован!')

        result = func(self, *args, **kwargs)

        self.health = old_health
        self.mana = old_mana

        print('Пасхальный бафф закончился')

        return result
    return wrapper


# Бафф посоха (только для волшебника)
def wizard_staff(func):
    def wrapper(self, *args, **kwargs):
        if self.hero_class == 'magic':
            self.mana += 5
            print('Священный посох дал +5 маны')

        result = func(self, *args, **kwargs)

        if self.hero_class == 'magic':
            self.mana -= 5

        return result
    return wrapper

def regen_after_action(func):
    '''После действия герой восстанавливает 2 HP'''
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        if self.health > 0:
            self.health += 2
            print(f'{self.name} восстановил 2 HP после действия')

        return result
    return wrapper

class Hero:
    def __init__(self, name, hero_class, spells_names=None, items=None):
        self.name = name
        self.hero_class = hero_class
        if hero_class == 'magic':
            self.health = 60
            self.mana = 50
        elif self.hero_class == 'warrior':  
            self.health = 100
            self.mana = 10
        self.spells_names = spells_names if spells_names else {}
        self.items = items if items else {}

    @is_alive
    @easter_buff
    @regen_after_action   
    def attack(self, damage):
        print(f'Герой нанес урон: {damage}')

    @log_action
    @regen_after_action   
    def heal(self, amount):
        self.health += amount
        print(f'{self.name} восстановил {amount} здоровья')

    @is_alive
    @wizard_staff
    @regen_after_action
    def cast_spell(self, spell_name):
        spell = self.spells_names.get(spell_name)
        
        if spell is None:
            print('Заклинание не изучено')
            return None

        if self.mana < spell['mana_cost']:
            print('Недостаточно маны')
            return None

        self.mana -= spell['mana_cost']
        print(f'{self.name} использует {spell_name}')

        if spell['attack_damage'] > 0:
            print(f"{self.name} наносит {spell['attack_damage']} урона")

        if spell['health_increase'] > 0:
            self.health += spell['health_increase']
            print(f"{self.name} восстанавливает {spell['health_increase']} здоровья")

    def add_spell(self, spell_name, mana_cost, attack_damage, health_increase):
        self.spells_names[spell_name] = {
            'mana_cost': mana_cost,
            'attack_damage': attack_damage,
            'health_increase': health_increase
        }

    def add_item(self, item_name, stat, value):
        if len(self.items) >= 6:
            print('Максимум 6 предметов')
            return None

        self.items[item_name] = {stat: value}

        if stat == "health":
            self.health += value
        elif stat == "mana":
            self.mana += value
