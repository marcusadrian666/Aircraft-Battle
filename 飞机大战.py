# 导入pygame模块
import pygame
# 导入random模块
import random
# 初始化pygame
pygame.init()
# 创建游戏窗口，大小为480*700
screen = pygame.display.set_mode((480, 700))
# 加载背景图片
bg = pygame.image.load("background.png")
# 绘制背景图片
screen.blit(bg, (0, 0))
# 加载英雄飞机图片
hero = pygame.image.load("me1.png")
# 绘制英雄飞机图片
screen.blit(hero, (200, 500))
# 更新屏幕显示
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 定义英雄飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)
# 创建敌机的精灵对象
enemy = pygame.sprite.Sprite()
# 加载敌机的图片
enemy.image = pygame.image.load("enemy1.png")
# 设置敌机的初始位置和速度
enemy.rect = enemy.image.get_rect()
enemy.rect.x = random.randint(0, 378)
enemy.rect.y = -39
enemy.speed = random.randint(1, 3)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)
# 创建子弹的精灵对象
bullet = pygame.sprite.Sprite()
# 加载子弹的图片
bullet.image = pygame.image.load("bullet1.png")
# 设置子弹的初始位置和速度
bullet.rect = bullet.image.get_rect()
bullet.rect.centerx = hero_rect.centerx
bullet.rect.bottom = hero_rect.top - 5
bullet.speed = -5
# 创建子弹的精灵组
bullet_group = pygame.sprite.Group(bullet)
# 设置游戏循环标志位
running = True
# 游戏循环
while running:
    # 设置刷新帧率为60帧/秒
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        # 判断是否退出游戏
        if event.type == pygame.QUIT:
            # 设置游戏循环标志位为False，退出循环
            running = False
        # 判断是否按下空格键，发射子弹
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # 创建新的子弹对象，添加到子弹组中
            new_bullet = pygame.sprite.Sprite()
            new_bullet.image = bullet.image
            new_bullet.rect = bullet.rect.copy()
            new_bullet.speed = bullet.speed
            bullet_group.add(new_bullet)
    # 获取按键状态，返回一个元组，表示所有按键的状态（按下为1，松开为0）
    keys_pressed = pygame.key.get_pressed()
    # 判断是否按下方向键，移动英雄飞机位置（边界检测）
    if keys_pressed[pygame.K_RIGHT]:
        hero_rect.x += 5
        if hero_rect.right > 480:
            hero_rect.right = 480
    elif keys_pressed[pygame.K_LEFT]:
        hero_rect.x -= 5
        if hero_rect.left < 0:
            hero_rect.left = 0 
    elif keys_pressed[pygame.K_UP]:
        hero_rect.y -= 5 
        if hero_rect.top < 0:
            hero_rect.top = 0 
    elif keys_pressed[pygame.K_DOWN]:
        hero_rect.y += 5 
        if hero_rect.bottom > 700:
            hero_rect.bottom = 700 
    # 绘制背景图片（覆盖之前绘制的内容）
    screen.blit(bg, (0, 0))
    # 绘制英雄飞机图片（覆盖之前绘制的内容）
    screen.blit(hero, hero_rect)
    # 更新敌机和子弹的位置（边界检测）
    enemy_group.update()
    bullet_group.update()
    # 绘制敌机和子弹的图片（覆盖之前绘制的内容）
    enemy_group.draw(screen)
    bullet_group.draw(screen)
    # 检测子弹和敌机是否发生碰撞（碰撞检测）
    enemies_hit = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
        # 如果有敌机被击中
    if enemies_hit:
        # 遍历被击中的敌机
        for enemy in enemies_hit:
            # 创建爆炸精灵对象，添加到爆炸精灵组中
            bomb = pygame.sprite.Sprite()
            bomb.image = pygame.image.load("enemy1_down1.png")
            bomb.rect = enemy.rect
            self.bomb_group.add(bomb)
    # 检测英雄飞机和敌机是否发生碰撞（碰撞检测）
    enemies_collided = pygame.sprite.spritecollide(hero, enemy_group, True)
    # 如果有敌机与英雄飞机碰撞
    if enemies_collided:
        # 创建英雄飞机爆炸精灵对象，添加到爆炸精灵组中
        hero_bomb = pygame.sprite.Sprite()
        hero_bomb.image = pygame.image.load("me_destroy_1.png")
        hero_bomb.rect = hero_rect
        self.hero_bomb_group.add(hero_bomb)
        # 设置游戏循环标志位为False，退出循环
        running = False
    # 绘制爆炸精灵的图片（覆盖之前绘制的内容）
    bomb_group.draw(screen)
    hero_bomb_group.draw(screen)
    # 更新屏幕显示（覆盖之前绘制的内容）
    pygame.display.update()
# 退出pygame
pygame.quit()
