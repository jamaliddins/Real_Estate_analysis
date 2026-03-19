Context
This SQLite database has been scraped from aqar.fm, which is a main source of real estate in Saudi Arabia where people go to share their real estate that is either for sale or rental.

This dataset contains all the publicly available listing data up to the date of collection (05/06/2023)

Content
Listings table:

id: integer, listing ID
uri: string,
title: string, listing title
price: integer, listing price in Saudi Riyal
content: text, listing description
imgs: text, JSON array of listing's array
refresh: integer, Unix timestamp indicating the last time this listing was refreshed by the user, in aqar users can refresh their listings to inform other users that it is still available
category: integer, id of a category (1= Apartment, rental | 2= Land, sell | 3= Villa, sell | 4= Floor, rental | 5= Villa, rental | 6= Apartment, sell | 7= Building, sell | 8= Store, rental | 9= House, sell | 10= Esterahah, sell | 11= House, rental | 12= Farm, sell | 13= Esterahah, rental | 14= Office, rental | 15= Land, rental | 16= Building, rental | 17= Warehouse, rental | 18= Campsite, rental | 19= Room, rental | 20= Store, sell | 21= Furnished apartment | 22= Floor, sell | 23= Chalet, rental)
beds: integer, count of beds in listing
livings: integer, count of living rooms in listing
wc: integer, count of bathrooms in listing
area: integer, area of the listing
type: integer
street_width: integer
age: integer, how old is this listing
last_update: integer, Unix timestamp
street_direction: integer
ketchen: integer, boolean if this listing has a kitchen or not (0 = false | 1 = true)
ac: integer, boolean if this listing has an air conditioning or not (0 = false | 1 = true)
furnished: integer, boolean if this listing is furnished or not (0 = false | 1 = true)
location.lat: float, location lattitude
location.lng: float, location longitude
path: string: path to the listing page
user.review: float, listing user reviews average
user.img: string, listing user img
user.name: string, listing user name
user.phone: string, listing user phone number
user.iam_verified: integer, boolean if the user listing it is verified or not (0 = false | 1 = true)
user.rega_id: integer
native.logo: string
native.title: string
native.image: string
native.description: string
native.external_url: string
rent_period: integer, id of a period (0: Yearly | 1: Daily | 2: Monthly | 3: Yearly)
city: string, listing's city in Arabic
city_id: integer, listing's city id
district: string, listing's district in Arabic
district_id: integer, listing's district id
width: integer, listing's width
length: integer, listing's length
advertiser_type: string, user type of the listing user
create_time: integer, Unix timestamp
has_extended_details: integer, boolean (0 = false | 1 = true)
daily_rentable: integer, boolean if this listing is daily rentable (0 = false | 1 = true)
Note on version 9 noted "Update 2026-02-09"
Missing width and length data of most entries after 2023-08
Removed createdAt and updatedAt columns as they are not necessary
Limited data between 2023-08 to 2025-03 as I had a long nice break from this project.
