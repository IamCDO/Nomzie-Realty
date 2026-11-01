from django.http import Http404
from django.shortcuts import render

PROPERTY_LISTINGS = [
    {
        'name': 'Insignia Properties',
        'slug': 'insignia',
        'location': 'Lagos, Nigeria',
        'image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297377/Insignia.jpg',
        'type': 'Luxury Homes',
        'tag': 'Featured',
    },
    {
        'name': 'Meridiana Gold Fold',
        'slug': 'meridiana-gold-fold',
        'location': 'Epe, Lagos',
        'image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297197/Meridiana_Gold_Fold.jpg',
        'type': 'Prime Estate',
        'tag': 'New Launch',
    },
    {
        'name': 'Meridiana Ketu',
        'slug': 'meridiana-ketu',
        'location': 'Ketu, Lagos',
        'image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297183/Meriadiana_Ketu.jpg',
        'type': 'Smart Living',
        'tag': 'Popular',
    },
    {
        'name': 'Meridiana Blue Oak',
        'slug': 'meridiana-blue-oak',
        'location': 'Epe, Lagos',
        'image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297104/Meridiana_Blue_Oak.jpg',
        'type': 'Lifestyle Estate',
        'tag': 'Exclusive',
    },
    {
        'name': 'Rivard Properties',
        'slug': 'rivard-properties',
        'location': 'Lekki, Lagos',
        'image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297086/Rivard.jpg',
        'type': 'Urban Homes',
        'tag': 'Top Pick',
    },
]

PROPERTY_DETAILS = {
    'insignia': {
        'title': 'INSIGNIA',
        'subtitle': 'Your preserve in SerenCity, Epe.',
        'hero_image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297377/Insignia.jpg',
        'intro': "Luxury is no longer a future conversation - it's officially here.",
        'body': [
            'Welcome to INSIGNIA - your preserve in SerenCity, Epe.',
            'A premium residential address created for those who value exclusivity, space, security, and long-term investment value.',
            'Location: Ejirin-Sekungba, Epe',
            'Title: Government Allocation/C of O',
            'Positioned within the rapidly developing Epe corridor and surrounded by landmark developments like the Lagos Food & Logistics Hub, Film City, and the proposed Lekki-Epe International Airport, INSIGNIA is designed for the future.',
            'This is more than land. This is legacy. This is premium living. This is INSIGNIA.'
        ],
        'sections': [
            {
                'heading': 'Plot and payment details',
                'items': ['Plot size: 750SQM', 'Price: NGN 60 Million', 'Flexible payment plan available'],
            },
        ],
        'cta_text': 'Book a Visit',
    },
    'meridiana-gold-fold': {
        'title': 'Meridiana Gold Fold',
        'subtitle': 'Omu Epe — where residential comfort meets commercial potential.',
        'hero_image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297197/Meridiana_Gold_Fold.jpg',
        'intro': 'Gold Fold Estate sits right on the express — opposite the African Food Logistics Hub. It’s designed as a smart blend of living and business in the heart of Lagos’ emerging economy.',
        'body': [
            'Location: Omu Epe (on the expressway)',
            'Title: Government Allocation',
            'Opposite the African Food Logistics Hub, and close to Film City, Yabatech, and Grace Polytechnic.',
            'Invest in a future-forward estate!'
        ],
        'sections': [
            {
                'heading': 'Plot sizes and prices',
                'items': [
                    '900SQM (Commercial): ₦35M',
                    '1500SQM (Premium Commercial): ₦70M',
                    '600SQM (Residential): ₦18M',
                    '450SQM (Residential): ₦15M',
                ],
            },
            {
                'heading': 'Estate features',
                'items': ['Paved roads and drainage', '24/7 security', 'Gated estate, solar lights, and green areas'],
            },
        ],
        'cta_text': 'Book a Visit',
    },
    'meridiana-blue-oak': {
        'title': 'Meridiana Blue Oak',
        'subtitle': 'Epe — where nature meets investment potential.',
        'hero_image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297104/Meridiana_Blue_Oak.jpg',
        'intro': "Welcome to luxury, where nature meets investment potential!",
        'body': [
            "Own land in one of Lagos' fastest-growing areas — Epe. Whether you're planning a dream home, a residential hub, or a commercial property, Blue Oak offers the perfect canvas.",
            'Location: Epe, Lagos',
            "Title: Government Allocation (C of O in view)",
            'This is your chance to invest in a location with guaranteed appreciation.'
        ],
        'sections': [
            {
                'heading': 'Plot sizes and prices',
                'items': ['600SQM: NGN 12 Million', '750SQM: NGN 20 Million'],
            },
            {
                'heading': 'Features',
                'items': [
                    'Perimeter fencing',
                    'Solar street lights',
                    'Paved roads',
                    'Play areas, tennis and basketball courts, and a clubhouse',
                    'Green spaces',
                ],
            },
        ],
        'cta_text': 'Book a Visit',
    },
    'meridiana-ketu': {
        'title': 'Meridiana Estate - Ketu, Epe',
        'subtitle': 'Peace, security, and long-term investment in Ketu-Epe.',
        'hero_image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297183/Meriadiana_Ketu.jpg',
        'intro': 'Looking for peace, security, and profit? You just found it.',
        'body': [
            'Meridiana Estate is located in the fast-rising Ketu-Epe axis, with direct access to Lekki-Epe Expressway and a link to Ikorodu. It is ideal for family living and long-term investment.',
            'Location: Ketu, Epe',
            'Title: Inclusive (with instant allocation)',
            'Close to African Food Hub, Film City, Saint Augustine University, and Grace Polytechnic.',
            'Peaceful living + fast ROI = a smart move!'
        ],
        'sections': [
            {
                'heading': 'Plot sizes and prices',
                'items': ['600SQM: NGN 15 Million', '300SQM: NGN 9 Million'],
            },
            {
                'heading': 'Features',
                'items': [
                    'Paved roads and solar lighting',
                    'Green relaxation areas',
                    'Flexible payment plan',
                    'Secure gated community',
                ],
            },
        ],
        'cta_text': 'Book a Visit',
    },
    'rivard-properties': {
        'title': 'Rivard Estate',
        'subtitle': 'Luxury living at the heart of the Mainland.',
        'hero_image': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297086/Rivard.jpg',
        'intro': 'An exclusive collection of 50 luxurious apartments on Apapa Road, Ebute-Metta, Lagos.',
        'body': [
            'Designed for those who appreciate comfort, convenience, quality, and long-term value, Rivard Estate combines contemporary architecture with practical urban living in an elegant, functional residential environment.',
            'Prime location: Apapa Road, Ebute-Metta, with access to major roads, commercial districts, business hubs, and everyday conveniences.',
            'For professionals, families, and investors seeking a strategic Mainland address, the location offers lifestyle convenience and real estate potential.',
            'Title: Registered Deed of Conveyance / Government Consent, providing documented ownership and a clear legal foundation for the investment.',
            'Rivard is more than an apartment - it is an opportunity to own part of a thoughtfully planned development in an established Mainland location.',
            'With only 50 apartments available, Rivard offers modern living without moving away from the established Mainland.'
        ],
        'sections': [
            {
                'heading': 'Apartment options',
                'items': [
                    '2-Bedroom Apartment: NGN 150 Million',
                    '3-Bedroom Apartment: NGN 180 Million',
                ],
            },
            {
                'heading': 'Key features and amenities',
                'items': [
                    'Beautifully designed modern apartments',
                    'Swimming pool for relaxation and leisure',
                    'Landscaped outdoor spaces',
                    'Well-planned communal areas',
                    'Contemporary architectural finishes',
                    'Spacious and functional living spaces',
                    'A serene residential environment within the Mainland',
                ],
            },
        ],
        'cta_text': 'Book a Visit',
    },
}


def home(request):
    context = {
        'logo_url': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297422/Logo.jpg',
        'properties': PROPERTY_LISTINGS,
    }
    return render(request, 'index.html', context)


def property_detail(request, slug):
    property_data = PROPERTY_DETAILS.get(slug)

    if property_data is None:
        raise Http404('Property details not found.')

    context = {
        'property': property_data,
        'logo_url': 'https://res.cloudinary.com/lbsccl1c/image/upload/v1793297422/Logo.jpg',
    }
    return render(request, 'property_detail.html', context)
