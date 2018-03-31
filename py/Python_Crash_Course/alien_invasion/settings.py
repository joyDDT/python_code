class Settings( ):
    """储存《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230,230,230)

        #飞船的位置
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor =3
        self.bullet_width =4
        self.bullet_height = 17
        self.bullet_color = 255,20,149
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        