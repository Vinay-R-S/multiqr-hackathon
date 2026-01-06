arr = [
    {
        "id": 1,
        "first_name": "Hershel",
        "last_name": "Andriss",
        "email": "handriss0@behance.net",
        "gender": "Male",
        "age": 68
    },
    {
        "id": 2,
        "first_name": "Goldia",
        "last_name": "Sunman",
        "email": "gsunman1@homestead.com",
        "gender": "Female",
        "age": 36
    },
    {
        "id": 3,
        "first_name": "Tobie",
        "last_name": "Dolan",
        "email": "tdolan2@msu.edu",
        "gender": "Male",
        "age": 20
    },
    {
        "id": 4,
        "first_name": "Chaunce",
        "last_name": "Fulep",
        "email": "cfulep3@nature.com",
        "gender": "Genderfluid",
        "age": 29
    },
    {
        "id": 5,
        "first_name": "Edlin",
        "last_name": "Martland",
        "email": "emartland4@altervista.org",
        "gender": "Male",
        "age": 33
    },
    {
        "id": 6,
        "first_name": "Nappy",
        "last_name": "Lanfear",
        "email": "nlanfear5@unblog.fr",
        "gender": "Male",
        "age": 46
    },
    {
        "id": 7,
        "first_name": "Maggie",
        "last_name": "Kilmary",
        "email": "mkilmary6@zimbio.com",
        "gender": "Female",
        "age": 58
    },
    {
        "id": 8,
        "first_name": "Kally",
        "last_name": "Marling",
        "email": "kmarling7@opensource.org",
        "gender": "Female",
        "age": 26
    },
    {
        "id": 9,
        "first_name": "Lucinda",
        "last_name": "Camacho",
        "email": "Icamacho8@whitehouse.gov",
        "gender": "Non-binary",
        "age": 24
    },
    {
        "id": 10,
        "first_name": "Maxine",
        "last_name": "Sawell",
        "email": "msawell9@bing.com",
        "gender": "Female",
        "age": 61
    },
    {
        "id": 11,
        "first_name": "Devon",
        "last_name": "Hub",
        "email": "dhuba@si.edu",
        "gender": "Female",
        "age": 37
    },
    {
        "id": 12,
        "first_name": "Lenette",
        "last_name": "Garside",
        "email": "Igarsideb@hhs.gov",
        "gender": "Female",
        "age": 21
    },
    {
        "id": 13,
        "first_name": "Trip",
        "last_name": "Leming",
        "email": "tlemingc@mysql.com",
        "gender": "Male",
        "age": 49
    },
    {
        "id": 14,
        "first_name": "Dill",
        "last_name": "Robak",
        "email": "drobakd@tinypic.com",
        "gender": "Male",
        "age": 43
    },
    {
        "id": 15,
        "first_name": "Nedi",
        "last_name": "Levins",
        "email": "nlevinse@cyberchimps.com",
        "gender": "Polygender",
        "age": 68
    },
    {
        "id": 16,
        "first_name": "Horacio",
        "last_name": "Mustin",
        "email": "hmustinf@amazon.de",
        "gender": "Genderqueer",
        "age": 45
    },
    {
        "id": 17,
        "first_name": "Dalis",
        "last_name": "Lambard",
        "email": "dlambardg@pen.io",
        "gender": "Male",
        "age": 32
    },
    {
        "id": 18,
        "first_name": "Lem",
        "last_name": "Abercromby",
        "email": "labercrombyh@admin.ch",
        "gender": "Male",
        "age": 34
    },
    {
        "id": 19,
        "first_name": "Nikkie",
        "last_name": "Dieton",
        "email": "ndietoni@hugedomains.com",
        "gender": "Female",
        "age": 48
    },
    {
        "id": 20,
        "first_name": "Leontine",
        "last_name": "Hockell",
        "email": "lhockellj@etsy.com",
        "gender": "Female",
        "age": 74
    }
]

console.log(arr.filter(item => item.age > 50).map(item => item.first_name));
