# database.py

# Structure: Category -> College Name -> { 'City': str, 'Website': str, 'Cutoffs': dict }
COLLEGE_DB = {
    "Engineering": {
        'COEP Tech University': {
            'City': 'Pune',
            'Website': 'https://www.coep.org.in/',
            'Cutoffs': {'CS': 99.8, 'EnTC': 99.2, 'Mech': 98.5, 'Meta': 96.0}
        },
        'VJTI Mumbai': {
            'City': 'Mumbai',
            'Website': 'https://www.vjti.ac.in/',
            'Cutoffs': {'CS': 99.7, 'IT': 99.5, 'EnTC': 99.0, 'Mech': 98.2, 'Textile': 96.0}
        },
        'SPIT Mumbai': {
            'City': 'Mumbai',
            'Website': 'https://www.spit.ac.in/',
            'Cutoffs': {'CS': 99.5, 'IT': 99.2, 'AI&DS': 99.0, 'EnTC': 98.5}
        },
        'PICT Pune': {
            'City': 'Pune',
            'Website': 'https://pict.edu/',
            'Cutoffs': {'CS': 99.4, 'IT': 99.1, 'AI&DS': 98.8, 'EnTC': 98.2}
        },
        'Walchand Sangli': {
            'City': 'Sangli',
            'Website': 'http://www.walchandsangli.ac.in/',
            'Cutoffs': {'CS': 98.8, 'IT': 98.2, 'EnTC': 97.5, 'Mech': 96.5, 'Civil': 95.0}
        },
        'D.J. Sanghvi': {
            'City': 'Mumbai',
            'Website': 'https://www.djsce.ac.in/',
            'Cutoffs': {'CS': 98.5, 'IT': 98.0, 'AI&DS': 97.8, 'EnTC': 96.5}
        },
        'Cummins College (Women)': {
            'City': 'Pune',
            'Website': 'https://www.cumminscollege.org/',
            'Cutoffs': {'CS': 97.5, 'IT': 96.5, 'EnTC': 94.0, 'Mech': 90.0}
        },
        'VIT Pune': {
            'City': 'Pune',
            'Website': 'https://www.vit.edu/',
            'Cutoffs': {'CS': 98.2, 'IT': 97.8, 'AI&DS': 97.5, 'EnTC': 96.0, 'Mech': 94.0}
        },
        'Thadomal Shahani': {
            'City': 'Mumbai',
            'Website': 'https://tsec.edu/',
            'Cutoffs': {'CS': 96.5, 'IT': 96.0, 'AI&DS': 95.5, 'EnTC': 93.0}
        },
        'PCCOE Pune': {
            'City': 'Pune',
            'Website': 'http://www.pccoepune.com/',
            'Cutoffs': {'CS': 97.5, 'IT': 97.0, 'EnTC': 95.5, 'Mech': 92.0}
        },
        'RCOEM Nagpur': {
            'City': 'Nagpur',
            'Website': 'http://www.rknec.edu/',
            'Cutoffs': {'CS': 96.0, 'IT': 95.5, 'AI&DS': 95.0, 'EnTC': 92.5}
        },
        'VIIT Pune': {
            'City': 'Pune',
            'Website': 'https://www.viit.ac.in/',
            'Cutoffs': {'CS': 95.5, 'IT': 94.5, 'EnTC': 91.0, 'Civil': 85.0}
        },
        'DY Patil Akurdi': {
            'City': 'Pune',
            'Website': 'https://www.dypcoeakurdi.ac.in/',
            'Cutoffs': {'CS': 95.0, 'IT': 94.5, 'AI&DS': 94.0, 'EnTC': 91.0, 'Civil': 82.0}
        },
        'K J Somaiya': {
            'City': 'Mumbai',
            'Website': 'https://kjsieit.somaiya.edu/',
            'Cutoffs': {'CS': 94.5, 'IT': 93.5, 'EnTC': 90.0, 'Mech': 85.0}
        },
        'Thakur College': {
            'City': 'Mumbai',
            'Website': 'https://www.tcetmumbai.in/',
            'Cutoffs': {'CS': 92.0, 'IT': 90.0, 'EnTC': 85.0, 'Mech': 75.0}
        },
        'AISSMS Pune': {
            'City': 'Pune',
            'Website': 'https://aissmscoe.com/',
            'Cutoffs': {'CS': 91.0, 'IT': 89.0, 'EnTC': 84.0, 'Mech': 78.0}
        },
        'Ramrao Adik (RAIT)': {
            'City': 'Mumbai',
            'Website': 'http://www.dypatil.edu/schools/engineering-and-technology',
            'Cutoffs': {'CS': 90.0, 'IT': 88.0, 'EnTC': 82.0, 'Mech': 75.0}
        },
        'MIT WPU': {
            'City': 'Pune',
            'Website': 'https://mitwpu.edu.in/',
            'Cutoffs': {'CS': 89.0, 'IT': 87.0, 'EnTC': 80.0, 'Mech': 70.0}
        },
        'Sinhgad Vadgaon': {
            'City': 'Pune',
            'Website': 'http://sinhgadsolapur.org/',
            'Cutoffs': {'CS': 85.0, 'IT': 82.0, 'EnTC': 75.0, 'Mech': 60.0}
        },
        # Special Recommendation
        'N.K. Orchid College Solapur': {
            'City': 'Solapur',
            'Website': 'https://orchidengg.ac.in/',
            'Cutoffs': {'CS': 70.0, 'Civil': 20.0, 'EnTC': 60.0, 'Mech': 40.0, 'Electrical': 50.0}
        }
    }
}