from client import AgenticCartBundleAffinityRecommenderClient

def main():
    client = AgenticCartBundleAffinityRecommenderClient()
    res = client.compute_cart_bundle_recommendations(['CAMERA_MIRRORLESS_BODY'])
    print('Cart Bundle Affinity Recommender: ' + res['recommendation_batch_id'])
    print('Cross-Sell SKUs: ' + str(len(res['recommended_cross_sell_skus'])) + ' items | Projected AOV Lift: +' + str(res['projected_aov_lift_pct']) + '%')
    print('Bundle Manifest: ' + res['bundle_deal_manifest_url'])

if __name__ == '__main__':
    main()
