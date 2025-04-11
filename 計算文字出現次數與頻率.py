# -*- coding: utf-8 -*-
"""計算文字出現次數與頻率.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nst4Y2589pwW1YUCuBaZMu3V8TFtDD5D
"""

import matplotlib.pyplot as plt
def x(file_path):
    dictionary = {}

    with open(file_path, 'r') as f:
        for line in f:
            word = line.strip()
            if word:

                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1

    print(f"1. 總共有 {len(dictionary)} 個不重複的英文字")
    print("2. 每一個英文字出現次數如下：")
    for word, count in dictionary.items():
        print(f"{word}: {count}")

    plt.figure(figsize=(10, 6))
    plt.bar(dictionary.keys(), dictionary.values())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

file_path = '/content/hw2_data.txt'
x(file_path)