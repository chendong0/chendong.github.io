import time
import os
import sys

def main(input_file_path, output_file_path):
    startTime = time.time()
    with open(input_file_path, mode='r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sorted_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)

    '''
    #找到for循环，其中包含word和count两个变量。
  删除count变量的引用，只保留word变量。
    '''

    with open(output_file_path, mode='w', encoding='utf-8') as f:
        for word, count in sorted_counts:
            f.write(f'{word} /  {count}\n')

    endTime = time.time()
    timeSpent = endTime - startTime
    print(f'Time spent: {timeSpent:.2f} seconds')
    sys.exit()
'''
程序中的一种常见写法，用于判断当前模块是否是主程序。如果当前模块是主程序，则执行if语句块中的代码；否则，不执行if语句块中的代码。
'''
if __name__ == "__main__":
    input_file_path = 'F:\\20231220\\software download\\20231228词性分析\\Obama-victory-speech.txt'
    output_file_path = 'F:\\20231220\\software download\\20231228词性分析\\Obama-victory-speechSplitCount.txt'
    main(input_file_path, output_file_path)
