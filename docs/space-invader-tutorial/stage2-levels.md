# 階段二:關卡系統(1:15–2:00)

> 🎯 **本階段目標**:再跑一次完整流程,但這次加入兩個專業習慣 —— **用 Issue 追蹤任務**、**用多個小 commit**。
> 解答在 [`solutions/stage2_levels.py`](../../solutions/stage2_levels.py)。

打完所有敵人遊戲就結束太可惜。我們讓它變成:清光一波 → **進入下一關**,敵人變快、關卡數 +1,可以一直玩下去。

---

## Step 1:先開一個 Issue(這次的新習慣)

在 GitHub repo 的 **Issues** 分頁 → **New issue**:

- 標題:`加入關卡系統`
- 內文:`清空敵人後重生一波,敵人速度 +1,畫面顯示目前關卡。`
- 建立後記下它的編號(例如 **#1**),等下 commit 會用到。

> Issue 就是「待辦事項 + 討論串」,團隊用它來分配與追蹤工作。

## Step 2:開分支

```bash
git checkout main
git pull
git checkout -b feature/levels
```

## Step 3:改程式

這次有四個地方,我們**分開 commit**,讓歷史更清楚。

**① 把生成敵人抽成函式(程式碼重用)**

找到 `reset_game()`,在它上面新增:

```python
def spawn_enemies():
    enemies = []
    for row in range(4):
        for col in range(8):
            enemies.append(pygame.Rect(60 + col * 60, 60 + row * 50, 40, 30))
    return enemies
```

然後讓 `reset_game()` 裡原本的雙層迴圈改成一行:

```python
    enemies = spawn_enemies()
```

➡️ **第一個 commit:**

```bash
git add space_invader.py
git commit -m "refactor: 把生成敵人抽成 spawn_enemies()"
```

**② 新增 `level` 變數**(在 `lives = 3` 附近)

```python
level = 1          # ⭐ 新增
```

**③ 把「清空就結束」改成「進下一關」**

找到:

```python
if not enemies:
    game_over = True
    win = True
```

改成:

```python
if not enemies:
    level += 1
    enemy_speed += 1          # 下一關更快
    bullets.clear()
    enemy_bullets.clear()
    enemies = spawn_enemies()
```

**④ 在畫面正上方顯示關卡**(畫分數那段附近)

```python
level_text = font.render(f"Level {level}", True, YELLOW)
screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 10))
```

> 記得在按 `R` 重新開始那段,把 `level = 1` 和 `enemy_speed = 1` 也加回去。

➡️ **第二個 commit:**

```bash
git add space_invader.py
git commit -m "feat: 加入關卡系統,清空後敵人加速重生 (Closes #1)"
```

> ✨ 訊息裡寫 `Closes #1`,等 PR merge 後,那個 Issue 會**自動關閉**!

## Step 4:測試

```bash
python space_invader.py
```

清光敵人,確認看到 `Level 2`、敵人變快、子彈被清空。

## Step 5:push + PR + merge + pull

```bash
git push -u origin feature/levels
```

然後跟階段一一樣:在 GitHub 開 PR → Merge → 回到本機:

```bash
git checkout main
git pull
```

merge 完去 **Issues** 分頁看一眼 —— 你的 #1 應該已經被自動關閉了。

---

## ✅ 完成檢查

- [ ] 清空一波後關卡數 +1、敵人變快
- [ ] `git log --oneline` 看得到兩個分開的 commit
- [ ] Issue #1 在 merge 後自動關閉

## 💡 你剛剛學到的

- **Issue** 怎麼追蹤任務、`Closes #編號` 怎麼自動收尾
- 為什麼要拆成**小 commit**:之後出問題,可以一個一個回溯,不會「一改全毀」
- 用 `git log --oneline` 讀自己的開發歷史
