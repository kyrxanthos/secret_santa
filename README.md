# Secret Santa Bot 🎁

This repo contains code that automatically sends a secret santa email to a list of participants.

## Setup

### Installation

1. Clone repo
2. `pip install -r requirements.txt`

### Setup gmail account

1. Go to your account settings and find the "Security" option.
Enable 2-step authentication
2. Now you will see an option "App Password". Create app password from there. It will be of 16 digits
3. Save this password and use it in the next step

### Run secret santa

1. create a `.env` file and add the following two variables:

```
ssUSERNAME=<gmail username>
ssPASSWORD=<password>
```

2. create a `SS_Data.csv` file with columns `Name` and `email` and populate `Name` with first and last name and `email` with corresponding email address.

3. Run secret santa with:

```
python secret_santa.py
```

Have fun 🎄🎅🎄

![alt text](dwight.gif)