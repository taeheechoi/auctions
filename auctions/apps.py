from django.apps import AppConfig


class AuctionsConfig(AppConfig):
    name = 'auctions'

class CustomAuctionsConfig(AppConfig):
    name = 'auctions'
    
    def ready(self):
        import auctions.signals
