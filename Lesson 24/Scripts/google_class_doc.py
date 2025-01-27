class SampleClass(object):
   """Здесь приводится общая информация о классе.

   Более детальная информация о классе....
   Более детальная информация о классе....

   Открытые атрибуты:
       likes_spam: Флаг, обозначающий любим ли мы спам или нет.
       letters: Целочисленный счетчик количества писем.
   """

   def __init__(self, likes_spam=False):
       """Инициализирует SampleClass..."""
       self.likes_spam = likes_spam
       self.letters = 0

   def public_method(self):
       """Выполняет операцию..."""

