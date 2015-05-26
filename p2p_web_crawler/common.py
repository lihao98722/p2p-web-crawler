__author__ = 'Howie'


domain_peer_ip_map = dict()


def get_peer_ip_by_domain(domain):
    return domain_peer_ip_map.get(domain, None)