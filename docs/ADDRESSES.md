# Darkspore.exe Addresses
Inside the game executable, there are the functions that make the game work. In order to make the game functional again, we have to understand what those functions are, and what they do. This is a list of the memory addresses that we already discover the purpose, and is also a reference for future findings. We have given provisory names to those functions and variables in order to make them more understandable from a developer perspective.

All the notes taken here consider only the latest official version of the game (5.3.0.127). Parameters named has `u*` have unknown purposes.

## Known functions

#### sub_401A80: allocStringWithSize
```cpp
void allocStringWithSize(void* stringPointer, unsigned int size) {(...)}
allocStringWithSize(&string, 0x11u);
```
Allocs in `stringPointer` a string with size `size`. No content is written in that space.

#### sub_402270: copyString
```cpp
void copyString(void* destination, void* source, int size) {(...)}
copyString(string, "version", 7);
```
Copies the contents of `source` to `destination`.

#### sub_402380: allocAndInitString
```cpp
void allocAndInitString(void* stringPointer, void* string) {(...)}
allocAndInitString(&string, "Version");
```
Allocs in `stringPointer` a string with `string`'s size +1, and writes `string` in that space.

#### sub_402FB0: stringWithFormat
```cpp
int __cdecl stringWithFormat(int destinationAddr, int formatAddr, char component);
stringWithFormat(&path, "/game/api?version=%u", 1);
```
Replaced `%` variables in `formatAddr` with `component` values, and store the result in `destinationAddr`. Replacement system works just like `printf`, for reference.

#### sub_40B6F0: copyString
```cpp
int __cdecl copyString(int destination, int source, u1)
copyString(&destination, &source, ?) {(...)}
```
Copy the contents of `source` to `destination`.

#### sub_43FF00: getValueFromXmlKey
```cpp
void* getValueFromXmlKey(void* valuePointer, void* u1, void* keyPointer) {(...)}
value = getValueFromXmlKey((keyAddr + keyAddrSize), ?, keyAddr);
```
Returns the string value of a XML key.

#### sub_45D810: getXmlValueForKey
```cpp
int getXmlValueForKey(void* xml, int key_begin_address, int u1, int u2, int u3) {(...)}
getXmlValueForKey(xml, key_begin_address, ?, ?, ?);
```
Returns the value of the mentioned key from the `xml` dictionary/map.

#### sub_45E310: retrieveAccountDetailsFromXmlObj
```cpp
void retrieveAccountDetailsFromXmlObj(void* account, int u1) {(...)}
retrieveAccountDetailsFromXmlObj(account, ?);
```
Read the account details from an `account` object retrieved from a xml dictionary/map.

#### sub_45EDE0: retrievePartsDetailsFromXmlObj
```cpp
void retrievePartsDetailsFromXmlObj(int response, void* parts) {(...)}
retrievePartsDetailsFromXmlObj(response, parts);
```
Read the parts details from a `parts` object retrieved from a xml dictionary/map, and store them in `response`.

#### sub_45F4C0: retrievePartsSimpleDetailsFromXmlObj
```cpp
void retrievePartsDetailsFromXmlObj(int response, void* parts) {(...)}
retrievePartsDetailsFromXmlObj(response, parts);
```
Read the parts details from a `parts` object retrieved from a xml dictionary/map, and store them in `response`.

#### sub_461600: getSurveysCallback
```cpp
void getSurveysCallback(int u1, void* xml) {(...)}
getSurveysCallback(?, xml);
```
The callback of the getSurveys function, with the returned `xml` dictionary/map.

#### sub_461EC0: bootstrapApiCallback
```cpp
char bootstrapApiCallback(int u1, void** u2, int u3, int u4) {(...)}
bootstrapApiCallback(?, ?, ?, ?)
```
The first step of all bootstrap/api functions responses.

#### sub_468120: retrieveBroadcastsDetailsFromXmlObj
```cpp
void retrieveBroadcastsDetailsFromXmlObj(int response, void* broadcasts) {(...)}
retrieveBroadcastsDetailsFromXmlObj(response, broadcasts);
```
Read the broadcasts details from a `broadcasts` object retrieved from a xml dictionary/map, and store them in `response`.

#### sub_469CE0: getBroadcastsCallback
```cpp
void getBroadcastsCallback(_DWORD* u1, void* xml) {(...)}
getBroadcastsCallback(?, xml);
```
The callback of the getBroadcasts function, with the returned `xml` dictionary/map.

#### sub_469E00: getStatusCallback
```cpp
void getStatusCallback(int u1, void* xml) {(...)}
getStatusCallback(?, xml);
```
The callback of the getStatus function, with the returned `xml` dictionary/map.

#### sub_46BDD0: getConfigsCallback
```cpp
void getConfigsCallback(void* configs, void* xml) {(...)}
getConfigsCallback(configs, xml);
```
The callback of the getConfigs function, with the returned `xml` dictionary/map, and store them in `configs`.

#### sub_7B3A20: setDarksporeVersion
```cpp
void setDarksporeVersion(char* version) {(...)}
setDarksporeVersion("5.3.0.127");
```
Saves the Darkspore version in `off_11444D4`, so it can be used in other places.

#### sub_ADF590: copyString
```cpp
int __cdecl copyString(int destination, int source, u1)
copyString(&destination, &source, ?) {(...)}
```
Copy the contents of `source` to `destination`.

#### sub_ADF6C0: copyString
```cpp
int __cdecl copyString(int destination, int source)
copyString(&destination, &source) {(...)}
```
Copy the contents of `source` to `destination`.

#### sub_AE44B0: stringToInteger
```cpp
unsigned long long stringToInteger(signed __int16* string, int* u1, signed int u2) {(...)}
integer = stringToInteger(string, ?, ?);
```
Parse `string` into an unsigned integer number.

#### sub_AE54C0: compareStrings
```cpp
char __cdecl compareStrings(int stringBeginAddr, int stringEndAddr, _WORD *stringToCompare, int u1);
result = compareStrings(&string, &string + 4, "Y", ?);
```
Compares two different strings. Returns `0` if the two strings are equal, like `strcmp`.

#### sub_B1C380: isAutodialEnabled
```cpp
bool isAutodialEnabled();
enabled = isAutodialEnabled();
```
Checks if autodial is enabled in the Windows registry.
**Note:** Microsoft Windows operating systems offer a networking feature that is convenient for users who use a modem to connect to the Internet: any TCP/IP request that occurs on the system activates an automatic modem dialing program.

#### sub_B1C3F0: setAutodialEnabled
```cpp
bool setAutodialEnabled(bool value);
setAutodialEnabled(true);
```
Set autodial to enabled/disabled in the Windows registry.

#### sub_C2D450: getter from dword_15E64F0
#### sub_C2D460: setter from dword_15E64F0

#### sub_BE49D0: setter from dword_15E5B30
#### sub_BE49E0: getter from dword_15E5B30

## Unknown functions

### Possibly connected with an event handler
- sub_4015B0
- sub_4015F0
- sub_551F10

### Possibly connected with the Blaze callback
- sub_C2D2B0
- sub_C2D370
- sub_C2A8D0
- sub_DEFED0
- sub_DF0520
- sub_DEC400
- sub_DEFED0
- sub_DF0520
- sub_E3E9A0
- sub_E415D0
- sub_E3E9A0
- sub_DEEA60
- sub_DEC1E0
- sub_DEDAC0
- sub_DEFE70
- sub_DF0050
- sub_C2A500
- sub_53AB80
- sub_5371F0
- sub_5373B0

### Possibly connected with the Blaze callback (login screen error handler)
- sub_E07760

### Deserves attention
- sub_AB42E0

## Known errors

### BlazeLoginManager errors
- sub_C465B0: Blaze login failed
- sub_C46610: Login SDK Error
- sub_C468D0: Error getting Nucleus Auth Token
- sub_C469B0: Login persona failed
- sub_C46A10: Create Persona Error
- sub_C46B00: Prepare for create account failed
- sub_C46B50: Create account failed

## Known strings
- off_10D9AEC: "gosredirector.online.ea.com"
- off_11444D4: Darkspore version ("5.3.0.127")
- off_FDB54C: "gms"
- off_FDB788: "false"
