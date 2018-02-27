
import googlemaps


class PlacesTest(_test.TestCase):

    def setUp(self):
        self.key = 'AIzaSyBPH6Eej16ErJTF7TLs-WC5sI9Vm9gd1VY'
        self.client = googlemaps.Client(self.key)
        self.location = (-33.86746, 151.207090)
        self.type = 'Hosppitals'
        self.language = 'en-AU'
        self.radius = 100

    

    @responses.activate
    def test_places_nearby_search(self):
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        responses.add(responses.GET, url,
                      body='{"status": "OK", "results": [], "html_attributions": []}',
                      status=200, content_type='application/json')

        self.client.places_nearby(self.location, keyword='foo',
                                  language=self.language, min_price=1,
                                  max_price=4, name='bar', open_now=True,
                                  rank_by='distance', type=self.type)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('%s?keyword=foo&language=en-AU&location=-33.86746%%2C151.20709&'
                            'maxprice=4&minprice=1&name=bar&opennow=true&rankby=distance&'
                            'type=liquor_store&key=%s'
                            % (url, self.key), responses.calls[0].request.url)

        with self.assertRaises(ValueError):
            self.client.places_nearby(self.location, rank_by="distance")

        with self.assertRaises(ValueError):
            self.client.places_nearby(self.location, rank_by="distance",
                                      keyword='foo', radius=self.radius)

    
