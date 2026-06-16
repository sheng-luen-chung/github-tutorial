# 階段三:防護罩 + 爆炸特效,並學會解決衝突(2:00–2:50)

> 🎯 **本階段目標**:做最有成就感的功能,並**故意製造一次 merge 衝突**讓你學會解決 —— 這是新手最怕、卻一定會遇到的關卡。
> 解答在 [`solutions/stage3_bunkers.py`](../../solutions/stage3_bunkers.py)。

---

## Part A:在 main 上製造一個「未來會衝突」的小改動

> 這一步是為了等下示範衝突,平常開發**不會**直接改 main,這裡是教學特例。

```bash
git checkout main
git pull
```

打開 `space_invader.py`,把分數的顏色從白色改成黃色:

```python
screen.blit(font.render(f"Score: {score}", True, YELLOW), (10, 10))
```

直接 commit 到 main 並 push:

```bash
git add space_invader.py
git commit -m "style: 分數改成黃色"
git push
```

## Part B:開分支做防護罩 + 爆炸,並改到「同一行」

```bash
git checkout -b feature/bunkers
```

### ① 防護罩

在 `spawn_enemies()` 下面新增生成防護罩的函式:

```python
CYAN = (0, 200, 200)

def spawn_bunkers():
    blocks = []
    block = 10
    for bunker in range(4):
        bx = 70 + bunker * 140
        by = HEIGHT - 150
        for row in range(3):
            for col in range(6):
                blocks.append(pygame.Rect(bx + col * block, by + row * block, block, block))
    return blocks
```

在 `reset_game()` 裡建立 bunkers,並把它一起回傳;主程式接收回傳值的那行、按 R 重開那行也要對應加上 `bunkers`。(完整寫法見解答檔)

在主迴圈的碰撞區,加入「子彈打掉防護罩方塊」:

```python
for b in bullets[:]:
    for blk in bunkers[:]:
        if b.colliderect(blk):
            bunkers.remove(blk)
            if b in bullets:
                bullets.remove(b)
            break
for eb in enemy_bullets[:]:
    for blk in bunkers[:]:
        if eb.colliderect(blk):
            bunkers.remove(blk)
            if eb in enemy_bullets:
                enemy_bullets.remove(eb)
            break
```

繪製區加上:

```python
for blk in bunkers:
    pygame.draw.rect(screen, CYAN, blk)
```

### ② 爆炸特效

新增清單 `explosions = []`(在 `level = 1` 附近)。
敵人被擊落時記下爆炸位置 —— 找到打中敵人那段,在 `enemies.remove(e)` 前加:

```python
explosions.append([e.centerx, e.centery, 2])   # [x, y, 半徑]
```

主迴圈更新爆炸(半徑變大、太大就消失):

```python
for ex in explosions[:]:
    ex[2] += 2
    if ex[2] > 18:
        explosions.remove(ex)
```

繪製:

```python
ORANGE = (255, 160, 0)
for ex in explosions:
    pygame.draw.circle(screen, ORANGE, (ex[0], ex[1]), ex[2])
```

### ③ 製造衝突點

把畫分數那行的顏色改成**青色**(故意跟 main 的黃色不同):

```python
screen.blit(font.render(f"Score: {score}", True, CYAN), (10, 10))
```

測試 → commit → push：

```bash
python space_invader.py            # 確認防護罩、爆炸都正常
git add space_invader.py
git commit -m "feat: 加入防護罩與擊落爆炸特效"
git push -u origin feature/bunkers
```

## Part C:開 PR → 遇到衝突 → 解決它

1. 在 GitHub 開 PR(base: `main` ← compare: `feature/bunkers`)。
2. 你會看到 **"This branch has conflicts that must be resolved"** —— 因為 main 和你的分支都改了畫分數那一行。
3. 我們在本機解決(比較好懂):

```bash
git checkout feature/bunkers
git pull origin main           # 把 main 的最新版併進來,這時會跳出衝突
```

打開 `space_invader.py`,找到長這樣的記號:

```python
<<<<<<< HEAD
        screen.blit(font.render(f"Score: {score}", True, CYAN), (10, 10))
=======
        screen.blit(font.render(f"Score: {score}", True, YELLOW), (10, 10))
>>>>>>> main
```

- `<<<<<<< HEAD` 到 `=======` 之間 = **你的版本**(青色)
- `=======` 到 `>>>>>>> main` 之間 = **main 的版本**(黃色)

**你來決定要哪個**。假設我們留青色,就把整段三個記號 + 不要的那行刪掉,只留:

```python
        screen.blit(font.render(f"Score: {score}", True, CYAN), (10, 10))
```

> ⚠️ 一定要把 `<<<<<<<`、`=======`、`>>>>>>>` 三行記號**全部刪乾淨**,它們不是程式碼,留著會壞掉。

解決後:

```bash
python space_invader.py        # 再跑一次確認沒壞
git add space_invader.py
git commit -m "merge: 解決分數顏色衝突,保留青色"
git push
```

回到 GitHub,PR 的衝突警告會消失,就能 **Merge** 了。merge 後:

```bash
git checkout main
git pull
```

## Part D:`.gitignore`(清掉不該上傳的檔案)

跑過遊戲後會多出 `__pycache__/` 資料夾,那是 Python 自動產生的,不該進版控。
專案根目錄已附上 [`.gitignore`](../../.gitignore),`git status` 就不會再看到它了。原理:列在 `.gitignore` 裡的東西,Git 會直接忽略。

---

## ✅ 完成檢查

- [ ] 防護罩會擋子彈、被打到會缺塊
- [ ] 擊落敵人有橘色爆炸
- [ ] 你親手解決過一次 merge 衝突並成功 merge
- [ ] `git status` 不再出現 `__pycache__/`

## 🎁 選做:加入音效

1. 找一個 `.wav` 音效檔(例如 [freesound.org](https://freesound.org)),放進 `assets/shoot.wav`。
2. 程式開頭:`shoot_sound = pygame.mixer.Sound("assets/shoot.wav")`
3. 發射子彈那行後面:`shoot_sound.play()`
4. 把 `assets/` **不要**寫進 `.gitignore`(音效要進版控),但記得確認檔案授權可自由使用。

## 💡 你剛剛學到的

- 衝突不可怕:它只是 Git 在問「這行你要哪個版本」
- `<<<<<<< ======= >>>>>>>` 三段記號怎麼讀、怎麼清
- `.gitignore` 為什麼存在
