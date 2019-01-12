## What it does ?
- It converts currency and returns it as a JSON file

## Requirements
- Python :
    - libraries :
        - Flask
        - termcolor
        - BeautifulSoup

## Parameters
- `amount` - amount which we want to convert - float
- `input_currency` - input currency - 3 letters name or currency symbol
- `output_currency` - requested/output currency - 3 letters name or currency symbol

## Output
- json with following structure.
```
{
    "input": { 
        "amount": <float>,
        "currency": < 3 letter currency code >
    }
    "output": {
        < 3 letter currency code >: <float>
    }
}
```
## Examples

### CLI 
```
python currency_convert.py --amount 100.0 --input_currency EUR --output_currency CZK
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2556.1123
    }
}

```
```
python currency_convert.py --amount 10.92 --input_currency £ 
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "AED": 51.54968348324188,
        "AFN": 1058.8985729572976,
        "ALL": 1539.7159375773867,
        .
        .
        .
        .
    }
}
```
### API
```
http://127.0.0.1:5000/currency_converter?amount=10.92&input_currency=£&output_currency=£

GET /currency_converter?amount=10.92&input_currency=%C2%A3&output_currency=%C2%A3 HTTP/1.1

{
  "input": {
    "amount": 10.92, 
    "currency": "GBP"
  }, 
  "output": {
    "GBP": 10.92
  }
}
```

```
http://127.0.0.1:5000/currency_converter?amount=10.92&input_currency=£

GET /currency_converter?amount=10.92&input_currency=%C2%A3 HTTP/1.1

{
  "input": {
    "amount": 10.92, 
    "currency": "GBP"
  }, 
  "output": {
    "AED": 51.54968348324188, 
    "AFN": 1058.8985729572976, 
    "ALL": 1539.7159375773867, 
    .
    .
    .
  }
}
```

## Supported Currencies
```
USD :  $ : US dollars
CAD :  CA$ : Canadian dollars
EUR :  € : euros
AED :  AED : UAE dirhams
AFN :  Af : Afghan Afghanis
ALL :  ALL : Albanian lekë
AMD :  AMD : Armenian drams
ARS :  AR$ : Argentine pesos
AUD :  AU$ : Australian dollars
AZN :  man. : Azerbaijani manats
BAM :  KM : Bosnia-Herzegovina convertible marks
BDT :  Tk : Bangladeshi takas
BGN :  BGN : Bulgarian leva
BHD :  BD : Bahraini dinars
BIF :  FBu : Burundian francs
BND :  BN$ : Brunei dollars
BOB :  Bs : Bolivian bolivianos
BRL :  R$ : Brazilian reals
BWP :  BWP : Botswanan pulas
BYR :  BYR : Belarusian rubles
BZD :  BZ$ : Belize dollars
CDF :  CDF : Congolese francs
CHF :  CHF : Swiss francs
CLP :  CL$ : Chilean pesos
CNY :  CN¥ : Chinese yuan
COP :  CO$ : Colombian pesos
CRC :  ₡ : Costa Rican colóns
CVE :  CV$ : Cape Verdean escudos
CZK :  Kč : Czech Republic korunas
DJF :  Fdj : Djiboutian francs
DKK :  Dkr : Danish kroner
DOP :  RD$ : Dominican pesos
DZD :  DA : Algerian dinars
EEK :  Ekr : Estonian kroons
EGP :  EGP : Egyptian pounds
ERN :  Nfk : Eritrean nakfas
ETB :  Br : Ethiopian birrs
GBP :  £ : British pounds sterling
GEL :  GEL : Georgian laris
GHS :  GH₵ : Ghanaian cedis
GNF :  FG : Guinean francs
GTQ :  GTQ : Guatemalan quetzals
HKD :  HK$ : Hong Kong dollars
HNL :  HNL : Honduran lempiras
HRK :  kn : Croatian kunas
HUF :  Ft : Hungarian forints
IDR :  Rp : Indonesian rupiahs
ILS :  ₪ : Israeli new sheqels
INR :  Rs : Indian rupees
IQD :  IQD : Iraqi dinars
IRR :  IRR : Iranian rials
ISK :  Ikr : Icelandic krónur
JMD :  J$ : Jamaican dollars
JOD :  JD : Jordanian dinars
JPY :  ¥ : Japanese yen
KES :  Ksh : Kenyan shillings
KHR :  KHR : Cambodian riels
KMF :  CF : Comorian francs
KRW :  ₩ : South Korean won
KWD :  KD : Kuwaiti dinars
KZT :  KZT : Kazakhstani tenges
LBP :  LB£ : Lebanese pounds
LKR :  SLRs : Sri Lankan rupees
LTL :  Lt : Lithuanian litai
LVL :  Ls : Latvian lati
LYD :  LD : Libyan dinars
MAD :  MAD : Moroccan dirhams
MDL :  MDL : Moldovan lei
MGA :  MGA : Malagasy Ariaries
MKD :  MKD : Macedonian denari
MMK :  MMK : Myanma kyats
MOP :  MOP$ : Macanese patacas
MUR :  MURs : Mauritian rupees
MXN :  MX$ : Mexican pesos
MYR :  RM : Malaysian ringgits
MZN :  MTn : Mozambican meticals
NAD :  N$ : Namibian dollars
NGN :  ₦ : Nigerian nairas
NIO :  C$ : Nicaraguan córdobas
NOK :  Nkr : Norwegian kroner
NPR :  NPRs : Nepalese rupees
NZD :  NZ$ : New Zealand dollars
OMR :  OMR : Omani rials
PAB :  B/. : Panamanian balboas
PEN :  S/. : Peruvian nuevos soles
PHP :  ₱ : Philippine pesos
PKR :  PKRs : Pakistani rupees
PLN :  zł : Polish zlotys
PYG :  ₲ : Paraguayan guaranis
QAR :  QR : Qatari rials
RON :  RON : Romanian lei
RSD :  din. : Serbian dinars
RUB :  RUB : Russian rubles
RWF :  RWF : Rwandan francs
SAR :  SR : Saudi riyals
SDG :  SDG : Sudanese pounds
SEK :  Skr : Swedish kronor
SGD :  S$ : Singapore dollars
SOS :  Ssh : Somali shillings
SYP :  SY£ : Syrian pounds
THB :  ฿ : Thai baht
TND :  DT : Tunisian dinars
TOP :  T$ : Tongan paʻanga
TRY :  TL : Turkish Lira
TTD :  TT$ : Trinidad and Tobago dollars
TWD :  NT$ : New Taiwan dollars
TZS :  TSh : Tanzanian shillings
UAH :  ₴ : Ukrainian hryvnias
UGX :  USh : Ugandan shillings
UYU :  $U : Uruguayan pesos
UZS :  UZS : Uzbekistan som
VEF :  Bs.F. : Venezuelan bolívars
VND :  ₫ : Vietnamese dong
XAF :  FCFA : CFA francs BEAC
XOF :  CFA : CFA francs BCEAO
YER :  YR : Yemeni rials
ZAR :  R : South African rand
ZMK :  ZK : Zambian kwachas
```