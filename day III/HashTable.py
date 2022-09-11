from random import randint

capacity = 10
hashTable = [[] for _ in range(capacity)]


def isPrime(n):
    if 1 == n or 0 == n:
        return True

    for i in range(2, n//2):
        if 0 == n % i:
            return True

    return False


def getPrime(n):
    if 0 == n % 2:
        n = n + 1

    while isPrime(n):
        n += 2

    return n


def hashFunction(key):
    return key % capacity


def insert(key, data):
    """Insert the key and data into the hash table

    Args:
        key (int): key
        data (Any): data
    """
    index = hashFunction(key)
    hashTable[index].append((key, data))


def remove(key):
    """Remove the tuple from the hash table (first occurrence)

    Args:
        key (int): key to search in the hash table

    Returns:
        tuple: first tuple that have the same key
    """
    idx_row = hashFunction(key)
    idx_col = -1

    for idx, record in enumerate(hashTable[idx_row]):
        k, v = record

        if k == key:
            idx_col = idx
            break

    return hashTable[idx_row].pop(idx_col)


def search(key):
    """Use the key to search for the tuple in the hash table

    Args:
        key (int): key to search in the hash table

    Returns:
        list: a list of tuple with the same key
    """
    index = hashFunction(key)
    result = []

    for record in hashTable[index]:
        k, v = record

        if k == key:
            result.append(record)

    return result


def random_string():
    result = ""

    for _ in range(randint(3, 10)):
        result += chr(randint(97, 122))

    return result


if __name__ == '__main__':
    minimum = 100
    maximum = 1000

    for _ in range(10000):
        key = randint(minimum, maximum)
        data = random_string()
        insert(key, data)
    print(hashTable)

    key_delete = randint(minimum, maximum)
    print(f'Removed: {remove(key_delete)}')
    print(hashTable)

    key_search = randint(minimum, maximum)
    print(f'Search for {key_search}: {search(key_search)}')
