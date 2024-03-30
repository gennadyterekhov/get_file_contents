def get_file_contents(filename: str)->str:
    handle = open(filename, 'r', encoding='utf8')
    content = handle.read()
    handle.close()
    return content

def put_file_contents(filename: str, data:str)->None:
    handle = open(filename, 'w', encoding='utf8')
    handle.write(data)
    handle.close()
