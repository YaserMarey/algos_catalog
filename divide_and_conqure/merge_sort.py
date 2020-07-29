# Merge sort
def merge_sort(A):
    if len(A) == 1:
        return A
    else:
        a = A[:int(len(A) / 2)]
        b = A[int(len(A) / 2):]
        a = merge_sort(a)
        b = merge_sort(b)
        c = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        c += a[i:]
        c += b[j:]
    return c

def main():
    A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    A = merge_sort(A)
    print(A)

if __name__ == '__main__':
    main()
