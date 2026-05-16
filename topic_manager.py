class TopicManager:
    @staticmethod
    def get_asset_topic(asset_type, asset_id):
        return f"microgrid/assets/{asset_type}/{asset_id}"

    @staticmethod
    def get_control_topic(action):
        return f"microgrid/control/{action}"