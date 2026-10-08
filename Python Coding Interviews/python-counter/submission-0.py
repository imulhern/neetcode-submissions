from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    s1_freq, s2_freq = Counter(s1), Counter(s2)
    s1_freq.update(s2_freq)
    return s1_freq
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
