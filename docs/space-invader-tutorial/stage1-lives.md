# 階段一:玩家三條命(0:30–1:15)

> 🎯 **本階段目標**:程式只改一點點,把全部注意力放在「完整跑一次 GitHub 流程」。
> 解答在 [`solutions/stage1_lives.py`](../../solutions/stage1_lives.py)。

現在的遊戲被打到一次就 GAME OVER,太硬了。我們讓玩家有 **3 條命**,右上角顯示還剩幾條。

---

## Step 1:開一條分支(永遠不要在 main 上改!)

```bash
git checkout main
git pull                       # 先確保 main 是最新的
git checkout -b feature/player-lives
```

> `-b` = 建立並切換到新分支。分支名用 `feature/做什麼`,一看就懂。

確認自己在新分支上:

```bash
git branch                     # 前面有 * 的就是目前分支
```

## Step 2:改程式(共三處)

打開 `space_invader.py`,做下面三個小修改。

**① 在分數變數附近,新增一個生命變數**

```python
score = 0
lives = 3          # ⭐ 新增
```

**② 把「被擊中就結束」改成「扣一條命」**

找到這段:

```python
for eb in enemy_bullets:
    if eb.colliderect(player):
        game_over = True
        win = False
```

改成:

```python
for eb in enemy_bullets[:]:                 # 加 [:] 是為了邊跑邊刪不出錯
    if eb.colliderect(player):
        enemy_bullets.remove(eb)            # 把打中的子彈移掉
        lives -= 1                          # 扣一條命
        if lives <= 0:
            game_over = True
            win = False
```

**③ 在畫面右上角顯示生命**(找到畫分數那行的下面)

```python
screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
# ⭐ 新增:
lives_text = font.render(f"Lives: {lives}", True, WHITE)
screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))
```

> 別忘了在按 `R` 重新開始的地方,也把 `lives = 3` 加回去,不然第二局只剩 0 條命。

## Step 3:測試

```bash
python space_invader.py
```

故意被打中三次,確認 Lives 從 3 → 2 → 1 → GAME OVER。

## Step 4:存檔快照(commit)

```bash
git status                     # 看看改了哪些檔案(會是紅色的)
git add space_invader.py
git commit -m "feat: 玩家三條命並顯示在右上角"
```

> 好的 commit 訊息開頭慣例:`feat:`(新功能)、`fix:`(修 bug)、`docs:`(改文件)。

## Step 5:上傳分支(push)

```bash
git push -u origin feature/player-lives
```

> `-u` 只有第一次推這條分支要加,之後直接 `git push` 就好。

## Step 6:開 Pull Request

1. 打開 GitHub 上的 repo,會看到一條黃色提示「Compare & pull request」,點它。
2. 標題寫:`玩家三條命`。
3. 內文簡單描述做了什麼(可參考 [templates.md](templates.md))。
4. 按 **Create pull request**。
5. 點 **Files changed** 分頁 —— 這就是別人 review 你程式碼時看的畫面,綠色是新增、紅色是刪除。
6. 按 **Merge pull request** → **Confirm merge**。🎉

## Step 7:把 main 同步回本機

```bash
git checkout main
git pull                       # 把剛剛 merge 進去的修改抓回來
```

---

## ✅ 完成檢查

- [ ] 遊戲裡看得到 `Lives: 3`,被打中會減少
- [ ] GitHub 上有一個已經 merge 的 PR
- [ ] 本機 main 分支跑遊戲也有三條命(代表 pull 成功)

## 💡 你剛剛學到的

你完整跑了一次 **branch → commit → push → PR → merge → pull**。
接下來兩個階段都是同一套,只是功能更難一點。流程,你已經會了。
