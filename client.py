class AgenticCartBundleAffinityRecommenderClient:
    def compute_cart_bundle_recommendations(self, active_cart_skus=['SKU_ESPRESSO_MACHINE_PRO'], max_bundle_recommendations=3):
        return {
            'recommendation_batch_id': 'bnd_rec_5519',
            'recommended_cross_sell_skus': [
                {'sku': 'SKU_BURR_GRINDER_STEEL', 'affinity_confidence_score': 0.94, 'bundled_discount_pct': 15},
                {'sku': 'SKU_BOTTOMLESS_PORTAFILTER', 'affinity_confidence_score': 0.88, 'bundled_discount_pct': 10}
            ],
            'projected_aov_lift_pct': 38.5,
            'bundle_deal_manifest_url': 'https://bundles.commerce.genpark.ai/deals/5519.json'
        }
