Title: Python Foundation
Date: 2019-09-08
Category: Python
Tags: Python Foundation


 
<details>
<summary>What is Bytes? </summary>
immutable sequences of bytes  
```python
b'data'
```
to convert between string and bytes, we must know the encoding of the byte sequence used to represent Unicode string  
Example:   
```python
data = "ABCD"
encodedData = data.encode('utf-8')
decodedData = encodedData.decode('utf-8')
```

Files, network resources, and HTTP responses are transmitted as **byte** streams
</details>
