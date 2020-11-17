class Random_Website():

    def __init__(self, site_details ={}, sites_by_ranked ={}):
        self.site_detail = site_details
        self.site_by_ranked = sites_by_ranked

    def set_sites_by_ranked(self, sites_by_ranked):
        print("got here")
        self.site_by_ranked = sites_by_ranked

    def get_site_by_value(self, value: int) -> dict:
        if value < self.site_by_ranked.__len__():
            return self.site_by_ranked[str(value)]
        else:
            return None
