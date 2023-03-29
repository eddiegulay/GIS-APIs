# GIS-APIs

## Map Box Usage

1. [open link]("https://docs.mapbox.com/playground/geocoding/")
2. Create account
3. Go back to playground then copy api key 

api_key looks like
* pk.eyJ1IjoiZWRkaWVndWxsZWQiLCJhIj......

## response sample

for a given addres list
```python
address_list = ['Mbeya', 'morogoro', 'Tanga']
```

Printed output
```python
['Mbeya, Tanzania', 33.468672, -8.906508]
['Mbeya, Tabora, Tanzania', 32.54364959, -4.509088225]
['Morogoro, Tanzania', 37.6693891, -6.8161626]
['Morogoro, Ruvuma, Tanzania', 35.416274071, -10.619590361]
['Marogoro, Pwani, Tanzania', 39.38738049, -7.100078789]
['Tanga, Tanzania', 39.0993457, -5.0721976]
['Tanga, Morogoro, Tanzania', 36.129998993, -8.874175353]
['Tanga, Ruvuma, Tanzania', 35.736243753, -10.587848198]
['Tanganyika, Morogoro, Tanzania', 35.62566516, -9.118546698]
```

