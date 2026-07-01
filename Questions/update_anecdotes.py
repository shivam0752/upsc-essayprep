import re

# File Paths
html_path = "d:/antigravity/projects/UPSC/Questions/anecdotes.html"
txt_path = "d:/antigravity/projects/UPSC/Questions/anecdotes.txt"
print_path = "d:/antigravity/projects/UPSC/Questions/anecdotes_print.html"

# Define the new anecdotes to insert into anecdotes.html
new_html_cards = [
    # 1. Ramanujan
    """      <!-- Card 13: Decision Making -->
      <div class="anecdote-card" data-category="decision">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Decision Making (Intuition & Logic)</span>
            <h3 class="card-title">Ramanujan's Intuitive Mock Theta Functions</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"Visionary decision-making happens at the intersection of intuition and logic." (UPSC 2023)</li>
              <li>"Thought finds a world and creates one also." (UPSC 2025)</li>
              <li>"Mathematics is the music of reason." (UPSC 2023)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            In the early 20th century, Srinivasa Ramanujan sat on the porch of his humble home in Kumbakonam, Tamil Nadu, armed only with a slate and red chalk. He lived in a world where formal mathematical proofs were the currency of credibility, a world he had not been formally trained to navigate. Yet, Ramanujan’s mind bypassed conventional logic. He claimed that the goddess Namagiri of Namakkal wrote complex mathematical equations on his tongue in dreams. Ramanujan did not just discover existing mathematical relations; his thoughts built entirely new paradigms. On his deathbed in 1920, with a failing body, he penned a letter to G.H. Hardy detailing what he called "Mock Theta Functions"—abstract mathematical constructs that did not fit into any known framework of his time. For nearly a century, these equations remained a mystery. It was only in the 2000s that physicists realized Ramanujan's mock theta functions are essential to calculating the entropy of black holes—cosmic phenomena that Ramanujan could not have observed. His mind found the abstract laws of numbers and, in doing so, created the framework to decode the deepest mysteries of the physical universe.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Ramanujan's mathematical breakthroughs show that visionary insights are often born from intuitive leaps that bypass conventional logic. In exploring how "thought finds a world and creates one also," his mock theta functions demonstrate that the mind can construct abstract frameworks that only later align with physical reality. Visionary decisions do not wait for established logic; they create the logic of the future.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">As we navigate complex administrative and intellectual challenges, we must honor the role of intuition alongside rigorous analysis. We must not discount the "goddess of Namakkal"—our creative hunches and deep insights—but rather use our logic to verify and build upon them, ensuring that our reasoning remains musical and creative.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Ramanujan</span>
            <span class="insight-badge">Intuitive Genius</span>
            <span class="insight-badge">Black Hole Entropy</span>
          </div>
        </div>
      </div>""",

    # 2. Gitanjali
    """      <!-- Card 14: Art & Spirit -->
      <div class="anecdote-card" data-category="art">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Art, Inspiration & Human Spirit</span>
            <h3 class="card-title">Tagore's Crucible of Gitanjali</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"Best lessons are learnt through bitter experiences." (UPSC 2025)</li>
              <li>"Poets are the unacknowledged legislators of the world." (UPSC 2022)</li>
              <li>"He who has a why to live for can bear almost any how." (Vajiram Test 3)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            Between 1902 and 1907, Rabindranath Tagore was pushed into a dark crucible of grief. In rapid succession, he lost his wife, Mrinalini Devi, his daughter, Renuka, and his youngest son, Shamindranath, who died of cholera at a tender age. The profound loneliness and raw pain of these bereavement years threatened to break his creative spirit. Instead of retreating into bitterness, Tagore channeled his grief into poetry. The songs of Gitanjali (Song Offerings) were born during this dark period. He transformed his deep personal sorrow into a universal quest for spiritual connection, translating the isolation of death into a deeper communion with the divine and the beauty of life. In 1913, Gitanjali won the Nobel Prize in Literature. It was not a product of intellectual comfort, but a wisdom refined by suffering. Tagore's bitterest losses taught him a profound empathy that resonated across the globe, illustrating that the human spirit learns its deepest truths not in the sunshine of prosperity, but in the shadows of adversity.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Tagore's creation of Gitanjali shows that the most profound artistic and human wisdom is often forged in the fires of personal grief. In discussing how "best lessons are learnt through bitter experiences," his poetry demonstrates that adversity does not have to break the human spirit; rather, it can serve as a catalyst to translate personal pain into universal empathy and art.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">As we face the inevitable setbacks and losses of life, we must remember the crucible of Gitanjali. We must channel our grief and adversity into creative, constructive action that serves the collective good. By finding a purpose (a "why") in our suffering, we can transcend our individual trials, contributing to the moral legislation of the world.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Tagore</span>
            <span class="insight-badge">Gitanjali</span>
            <span class="insight-badge">Resilience through Art</span>
          </div>
        </div>
      </div>""",

    # 3. Lao Tzu (Wu-Wei)
    """      <!-- Card 15: Wisdom & Time -->
      <div class="anecdote-card" data-category="wisdom">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Wisdom & Time</span>
            <h3 class="card-title">Lao Tzu and the Principle of Wu-Wei</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"Muddy water is best cleared by leaving it alone." (UPSC 2025)</li>
              <li>"The years teach much which the days never know." (UPSC 2025)</li>
              <li>"Best for an individual is not necessarily best for the society." (UPSC 2019)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            In ancient China, during the chaotic Warring States period, the philosopher Lao Tzu observed rulers attempting to fix social decay through aggressive regulation, heavy taxes, and constant military interventions. He likened their hyperactive governance to a person trying to clear a muddy pool by stirring it with a stick—an action that only suspended the sediment further. Lao Tzu introduced the concept of Wu-Wei (effortless action or non-interference). To demonstrate this to his disciples, he told a story of a traveler who came across a stream churned up by a passing horse carriage. The disciple eagerly offered to step in and filter out the mud. Lao Tzu stopped him and said, "Wait." They sat in silence. Slowly, gravity pulled the mud down. The leaves settled. Within an hour, the water was crystal clear and fit to drink. In public policy, this is often seen in the contrast between over-regulation and letting organic markets or communities self-regulate. When the state over-intervenes in complex systems, it creates noise; sometimes, the wisest policy is to create the space for natural equilibrium to restore itself.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Lao Tzu's metaphor of the churned stream demonstrates that some complex problems are best solved not through restless, aggressive intervention, but through patient, deliberate inaction (Wu-Wei). In discussing how "muddy water is best cleared by leaving it alone," his philosophy highlights that over-regulation and hasty interference often exacerbate social friction rather than resolving it, whereas allowing systems to settle naturally restores harmony.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">In managing modern administrative and social challenges, we must learn when to step back and let the mud settle. By trusting the natural equilibrium of communities and letting the sediment of hasty decisions sit under the influence of time, we can ensure that our policy decisions are clear, stable, and sustainable, rather than continuously churned up by the stick of over-intervention.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Lao Tzu</span>
            <span class="insight-badge">Wu-Wei</span>
            <span class="insight-badge">Public Restraint</span>
          </div>
        </div>
      </div>""",

    # 4. Kabir Shroud of Flowers
    """      <!-- Card 16: Truth & Integrity -->
      <div class="anecdote-card" data-category="truth">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Truth & Integrity</span>
            <h3 class="card-title">Kabir's Shroud of Flowers</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"Truth knows no color." (UPSC 2025)</li>
              <li>"Values are not what humanity is, but what humanity ought to be." (UPSC 2019)</li>
              <li>"Your perception of me is a reflection of you; my reaction to you is an awareness of me." (UPSC 2021)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            In the humid, dust-choked lanes of 15th-century Varanasi, the Bhakti mystic Kabir composed verses that cut clean through the sectarian divide of medieval India. To the Hindu orthodoxy, truth was colored in the saffron of rituals, caste hierarchies, and Sanskrit scriptures. To the Islamic clergy, truth was wrapped in the green of formal dogmas, Arabic texts, and institutionalized power. Kabir rejected both, declaring that the ultimate reality was an unpainted, formless presence—Nirguna. Upon Kabir's death in Maghar, a fierce dispute erupted. The Hindus demanded his body for cremation, claiming him as their guru; the Muslims insisted on burial, claiming him as their Sufi Pir. As the confrontation grew violent, someone drew back the white shroud covering his body. To their absolute bewilderment, the corpse had vanished. In its place lay a heap of fresh, fragrant flowers. Dumbfounded, the two groups divided the flowers. The Hindus cremated their share; the Muslims buried theirs. The colors of their rites remained different, but the entity they sought to possess had transitioned beyond both, proving that Truth belongs to no single faction.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">The legend of Kabir's death illustrates that ultimate truth knows no color—it cannot be contained within the sectarian boundaries of religion, language, or culture. In exploring how "truth knows no color," this story reveals that when we attempt to divide reality into opposing factions, we lose the essence of the truth itself. True values exist not in our tribal divisions, but in the syncretic space that unites us.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">As we navigate a society divided by identity politics and cultural conflicts, we must remember the shroud of flowers at Maghar. We must seek the common ground that lies beneath our different rites and beliefs. By treating truth as a formless, shared reality rather than a colored banner to be fought over, we can build a nation that values unity and mutual respect.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Kabir</span>
            <span class="insight-badge">Nirguna Truth</span>
            <span class="insight-badge">Sectarian Unity</span>
          </div>
        </div>
      </div>""",

    # 5. George Dantzig
    """      <!-- Card 17: Knowledge & Education -->
      <div class="anecdote-card" data-category="knowledge">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Knowledge & Education</span>
            <h3 class="card-title">George Dantzig and the Impossible Homework</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"What is research, but a blind date with knowledge!" (UPSC 2021)</li>
              <li>"Thought finds a world and creates one also." (UPSC 2025)</li>
              <li>"Experience without theory is blind, but theory without experience is mere intellectual play." (Vajiram Test 1)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            One day, when George Dantzig was a graduate student at the University of California, Berkeley, he arrived late to his statistics class. On the board, the professor had written two very difficult problems. Dantzig thought they were homework questions. He copied them down and went home. The problems looked very hard, so he worked on them for several days. Finally, he solved them and submitted the answers to his professor, Jerzy Neyman. A few weeks later, the professor came to Dantzig’s house very excited. He told him something surprising: those two problems were not homework. They were actually unsolved problems in statistics, which many mathematicians had been trying to solve for years. Without knowing they were “impossible,” Dantzig solved them.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Dantzig’s breakthrough shows that the perception of what is "impossible" is often a cognitive barrier that prevents discovery. In exploring how "research is a blind date with knowledge," his story reveals that when we approach a problem without the burden of historical failure, we can find solutions that others hesitated to try. Belief and effort are far more powerful than the rules of conventional wisdom.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">In our educational and policy efforts, we must encourage students to challenge the limits of what is considered possible. We must ensure that our research environments do not crush independent thinking under the weight of established dogma. By letting our students date knowledge blindly—without telling them which problems are unsolvable—we can unlock new paths to progress.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">George Dantzig</span>
            <span class="insight-badge">Solving the Impossible</span>
            <span class="insight-badge">Cognitive Barriers</span>
          </div>
        </div>
      </div>""",

    # 6. Jeremiah Denton
    """      <!-- Card 18: Courage & Fortitude -->
      <div class="anecdote-card" data-category="courage">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Courage & Fortitude</span>
            <h3 class="card-title">Jeremiah Denton's Morse Code Blinking</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"Courage to accept and dedication to improve are two keys to success." (UPSC 2019)</li>
              <li>"In a time of universal deceit, telling the truth is a revolutionary act." (Vajiram Test 3)</li>
              <li>"A ship in harbour is safe, but that is not what a ship is for." (UPSC 2022)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            During the Vietnam War, Captain Jeremiah Denton was captured by North Vietnamese forces and kept as a prisoner of war (POW) for several years. He was often tortured and forced to appear in propaganda videos. In 1966, the captors made him appear on television to show the world that American prisoners were being treated well. While answering questions, Denton seemed calm and obedient. But he did something very clever. As he spoke, he blinked his eyes repeatedly. It looked like he was just struggling with the bright lights, but in reality he was using Morse code with his blinking. He blinked the word: T-O-R-T-U-R-E. Through this secret message, he informed the U.S. government that American prisoners in Vietnam were being tortured. This became the first confirmed evidence of the mistreatment of American POWs in North Vietnam.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Jeremiah Denton’s blinking Morse code is a powerful example of moral courage and presence of mind under extreme pressure. In discussing how "telling the truth in a time of universal deceit is a revolutionary act," his story shows that even when physically bound and silenced, an individual can find creative, subtle ways to stand by their truth.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">Denton's silent blinks remind us that our integrity cannot be imprisoned unless we choose to surrender it. When we face environments of censorship or systemic dishonesty, we must use our intelligence to find ways to speak the truth. By maintaining our moral alignment even under coercion, we keep the light of truth burning.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Jeremiah Denton</span>
            <span class="insight-badge">Morse Code Blinks</span>
            <span class="insight-badge">Resilience</span>
          </div>
        </div>
      </div>""",

    # 7. Ernest Shackleton
    """      <!-- Card 19: Courage & Fortitude -->
      <div class="anecdote-card" data-category="courage">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Courage & Fortitude</span>
            <h3 class="card-title">Ernest Shackleton's Rescue Mission</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"Character of an institution is reflected in its leader." (UPSC 2015)</li>
              <li>"He who has a why to live for can bear almost any how." (Vajiram Test 3)</li>
              <li>"Best lessons are learnt through bitter experiences." (UPSC 2025)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            In 1915, British explorer Ernest Shackleton set out on an ambitious expedition to cross Antarctica. His ship, Endurance, however, became trapped in thick Antarctic ice. After months of pressure from the ice, the ship was eventually crushed and sank, leaving Shackleton and his crew stranded in one of the harshest environments on Earth. With freezing temperatures, limited food, and no chance of immediate rescue, the situation looked hopeless. At that moment, Shackleton made a remarkable decision. He abandoned the mission of exploration and announced a new goal to his crew: "The expedition is over. Now our mission is to get everyone home alive." For months, Shackleton kept the crew motivated and united. He carefully rationed food, maintained discipline, and constantly lifted the morale of his men. Even when they had to survive on drifting ice and later make a dangerous journey across the stormy Southern Ocean in small boats, Shackleton never allowed despair to take over. After nearly two years of struggle, he successfully organized a rescue mission. Remarkably, every single member of the expedition survived.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Shackleton's leadership during the Endurance crisis shows that a leader's character is tested not in moments of victory, but in how they manage failure and prioritize their team. In exploring how "he who has a why to live for can bear almost any how," his decision to shift focus from ambition to survival gave his men a collective purpose that kept hope alive in the coldest abyss.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">In our modern institutions and enterprises, leadership must prioritize human life and collective well-being over raw target acquisition. By maintaining morale, discipline, and unity during crises, leaders can guide their teams through the most hostile environments, proving that a leader's true legacy is the safety and integrity of their people.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Ernest Shackleton</span>
            <span class="insight-badge">Endurance Expedition</span>
            <span class="insight-badge">Crisis Leadership</span>
          </div>
        </div>
      </div>""",

    # 8. Bruce Lee
    """      <!-- Card 20: Courage & Fortitude -->
      <div class="anecdote-card" data-category="courage">
        <div class="card-header">
          <div class="card-header-left">
            <span class="theme-badge">Courage & Fortitude</span>
            <h3 class="card-title">Bruce Lee's "Be Like Water" Recovery</h3>
          </div>
          <button class="card-action-btn" onclick="copyCardContent(this)"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Text</button>
        </div>
        <div class="card-body">
          <div class="mapped-questions">
            <div class="mapped-questions-title">Mapped Prompts</div>
            <ul class="mapped-questions-list">
              <li>"That which does not kill us makes us stronger." (Vajiram Test 2)</li>
              <li>"A ship in harbour is safe, but that is not what a ship is for." (UPSC 2022)</li>
              <li>"Courage to accept and dedication to improve are two keys to success." (UPSC 2019)</li>
            </ul>
          </div>
          <div class="anecdote-narrative">
            In the early 1970s, at the peak of his physical prowess, Bruce Lee suffered a severe back injury during a training session. Doctors told him he might never practice martial arts again. For someone whose identity revolved around movement, strength, and discipline, this was devastating. Instead of giving up, Bruce Lee adapted. Confined to bed for months, he began writing extensively—refining his philosophy of life and martial arts. It was during this period that he deeply articulated his famous idea: "Be like water." Water, he believed, does not resist obstacles—it flows around them, adjusts, reshapes, yet remains powerful. Against all odds, Bruce Lee not only recovered but returned stronger—physically and mentally. He went on to revolutionize martial arts and global cinema.
          </div>
          <div class="essay-blocks">
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg> Intro Pivot</div>
              <div class="block-content">Bruce Lee’s recovery reveals that resilience is not merely physical toughness, but the mental capacity to adapt to constraints. In discussing the "courage to accept and dedication to improve," his bedridden months show that when our physical paths are blocked, we must reshape our efforts, finding new avenues for growth rather than giving up.</div>
            </div>
            <div class="block-panel">
              <div class="section-title"><svg viewBox="0 0 24 24"><path d="M10 9H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-5M12 2v12M12 2L8 6M12 2l4 4"></path></svg> Outro Callback</div>
              <div class="block-content">As we encounter the inevitable obstacles of our lives, we must strive to be like water. Instead of breaking against the barriers of adversity, we must flow around them, using constraints as opportunities to refine our minds and characters, ensuring that we return stronger and more adaptable.</div>
            </div>
          </div>
          <div class="key-insights">
            <span class="insight-badge">Bruce Lee</span>
            <span class="insight-badge">Be Like Water</span>
            <span class="insight-badge">Adaptability</span>
          </div>
        </div>
      </div>"""
]

# Update anecdotes.html
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the anecdotes list closing tag to append the new cards before it
# We look for the closing div tag of <div class="anecdotes-list" id="anecdotesList">
# The list has a structure where all Cards are siblings inside id="anecdotesList".
# We can find the comment <!-- Card 12: Art --> or similar, or find the no-results div.
# Let's see: the list ends right before:
#     </div>
# 
#     <!-- No Results -->
#     <div class="no-results" id="noResults">
target_search = """    <!-- No Results -->
    <div class="no-results" id="noResults">"""

cards_to_insert = "\\n\\n".join(new_html_cards) + "\\n\\n"
new_content_to_replace = cards_to_insert + "    </div>\\n\\n    <!-- No Results -->\\n    <div class=\"no-results\" id=\"noResults\">"

# Check if these cards are already added
if "Ramanujan's Intuitive Mock Theta Functions" not in html_content:
    # Find the last closing </div> of the anecdotesList
    # Let's find the last occurrence of "      </div>\\n\\n    </div>\\n\\n    <!-- No Results -->"
    # Actually, the last card ends with "        </div>\\n      </div>" followed by a closing "    </div>" for anecdotesList
    # Let's do a search and replace on the exact boundary
    match = re.search(r'\\s+</div>\\s+</div>\\s+</div>\\s+<!-- No Results -->', html_content)
    if match:
        html_content = html_content.replace("      </div>\\n\\n    </div>\\n\\n    <!-- No Results -->", "      </div>\\n\\n" + cards_to_insert + "    </div>\\n\\n    <!-- No Results -->")
        print("Updated anecdotes.html successfully!")
    else:
        # Alternative fallback replace
        html_content = html_content.replace("    <!-- No Results -->", cards_to_insert + "    <!-- No Results -->")
        # We need to add back the closing </div> if it was misplaced, but let's be careful.
        # Let's inspect the file structure or simply do a robust regex insert.
        print("Using fallback replace for anecdotes.html")
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
else:
    print("anecdotes.html already contains the new cards.")

# Now let's update anecdotes.txt
with open(txt_path, 'r', encoding='utf-8') as f:
    txt_content = f.read()

new_txt_entries = [
    # 1. Ramanujan
    """--------------------------------------------------------------------------------
Anecdote 5D: Ramanujan's Intuitive Mock Theta Functions (Intuitive / Science)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "Visionary decision-making happens at the intersection of intuition and logic." (UPSC 2023)
  - "Thought finds a world and creates one also." (UPSC 2025)
  - "Mathematics is the music of reason." (UPSC 2023)

* Narrative:
  In the early 20th century, Srinivasa Ramanujan sat on the porch of his humble 
  home in Kumbakonam, Tamil Nadu, armed only with a slate and red chalk. He lived 
  in a world where formal mathematical proofs were the currency of credibility, 
  a world he had not been formally trained to navigate. Yet, Ramanujan’s mind 
  bypassed conventional logic. He claimed that the goddess Namagiri of Namakkal 
  wrote complex mathematical equations on his tongue in dreams. Ramanujan did not 
  just discover existing mathematical relations; his thoughts built entirely new 
  paradigms. On his deathbed in 1920, with a failing body, he penned a letter to 
  G.H. Hardy detailing what he called "Mock Theta Functions"—abstract mathematical 
  constructs that did not fit into any known framework of his time. For nearly 
  a century, these equations remained a mystery. It was only in the 2000s that 
  physicists realized Ramanujan's mock theta functions are essential to calculating 
  the entropy of black holes—cosmic phenomena that Ramanujan could not have observed. 
  His mind found the abstract laws of numbers and, in doing so, created the 
  framework to decode the deepest mysteries of the physical universe.

* Thesis Pivot (Intro Hook):
  Ramanujan's mathematical breakthroughs show that visionary insights are often 
  born from intuitive leaps that bypass conventional logic. In exploring how 
  "thought finds a world and creates one also," his mock theta functions 
  demonstrate that the mind can construct abstract frameworks that only later 
  align with physical reality. Visionary decisions do not wait for established 
  logic; they create the logic of the future.

* Callback & Philosophical Elevation (Conclusion):
  As we navigate complex administrative and intellectual challenges, we must 
  honor the role of intuition alongside rigorous analysis. We must not discount 
  the "goddess of Namakkal"—our creative hunches and deep insights—but rather 
  use our logic to verify and build upon them, ensuring that our reasoning 
  remains musical and creative.

* Key Insights:
  - Intuitive mathematical leaps.
  - Theory preceding empirical observation by a century.
  - Cultivating non-formal paths of knowledge.""",

    # 2. Gitanjali
    """--------------------------------------------------------------------------------
Anecdote 12D: Tagore's Crucible of Gitanjali (Art / Inspiration)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "Best lessons are learnt through bitter experiences." (UPSC 2025)
  - "Poets are the unacknowledged legislators of the world." (UPSC 2022)
  - "He who has a why to live for can bear almost any how." (Vajiram Test 3)

* Narrative:
  Between 1902 and 1907, Rabindranath Tagore was pushed into a dark crucible of 
  grief. In rapid succession, he lost his wife, Mrinalini Devi, his daughter, 
  Renuka, and his youngest son, Shamindranath, who died of cholera at a tender age. 
  The profound loneliness and raw pain of these bereavement years threatened to 
  break his creative spirit. Instead of retreating into bitterness, Tagore channeled 
  his grief into poetry. The songs of Gitanjali (Song Offerings) were born during 
  this dark period. He transformed his deep personal sorrow into a universal quest 
  for spiritual connection, translating the isolation of death into a deeper 
  communion with the divine and the beauty of life. In 1913, Gitanjali won the 
  Nobel Prize in Literature. It was not a product of intellectual comfort, but 
  a wisdom refined by suffering. Tagore's bitterest losses taught him a profound 
  empathy that resonated across the globe, illustrating that the human spirit 
  learns its deepest truths not in the sunshine of prosperity, but in the 
  shadows of adversity.

* Thesis Pivot (Intro Hook):
  Tagore's creation of Gitanjali shows that the most profound artistic and human 
  wisdom is often forged in the fires of personal grief. In discussing how 
  "best lessons are learnt through bitter experiences," his poetry demonstrates 
  that adversity does not have to break the human spirit; rather, it can serve 
  as a catalyst to translate personal pain into universal empathy and art.

* Callback & Philosophical Elevation (Conclusion):
  As we face the inevitable setbacks and losses of life, we must remember the 
  crucible of Gitanjali. We must channel our grief and adversity into creative, 
  constructive action that serves the collective good. By finding a purpose 
  (a "why") in our suffering, we can transcend our individual trials, contributing 
  to the moral legislation of the world.

* Key Insights:
  - Transforming grief into artistic beauty.
  - Wisdom refined by suffering.
  - The power of global empathy forged in adversity.""",

    # 3. Lao Tzu
    """--------------------------------------------------------------------------------
Anecdote 2D: Lao Tzu's Churned Stream (Wisdom / Time)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "Muddy water is best cleared by leaving it alone." (UPSC 2025)
  - "The years teach much which the days never know." (UPSC 2025)
  - "Best for an individual is not necessarily best for the society." (UPSC 2019)

* Narrative:
  In ancient China, during the chaotic Warring States period, the philosopher 
  Lao Tzu observed rulers attempting to fix social decay through aggressive 
  regulation, heavy taxes, and constant military interventions. He likened their 
  hyperactive governance to a person trying to clear a muddy pool by stirring it 
  with a stick—an action that only suspended the sediment further. Lao Tzu 
  introduced the concept of Wu-Wei (effortless action or non-interference). To 
  demonstrate this to his disciples, he told a story of a traveler who came across 
  a stream churned up by a passing horse carriage. The disciple eagerly offered 
  to step in and filter out the mud. Lao Tzu stopped him and said, "Wait." They 
  sat in silence. Slowly, gravity pulled the mud down. The leaves settled. 
  Within an hour, the water was crystal clear and fit to drink. In public policy, 
  this is often seen in the contrast between over-regulation and letting organic 
  markets or communities self-regulate. When the state over-intervenes in 
  complex systems, it creates noise; sometimes, the wisest policy is to create the 
  space for natural equilibrium to restore itself.

* Thesis Pivot (Intro Hook):
  Lao Tzu's metaphor of the churned stream demonstrates that some complex 
  problems are best solved not through restless, aggressive intervention, but 
  through patient, deliberate inaction (Wu-Wei). In discussing how "muddy water 
  is best cleared by leaving it alone," his philosophy highlights that over-regulation 
  and hasty interference often exacerbate social friction rather than resolving 
  it, whereas allowing systems to settle naturally restores harmony.

* Callback & Philosophical Elevation (Conclusion):
  In managing modern administrative and social challenges, we must learn when 
  to step back and let the mud settle. By trusting the natural equilibrium of 
  communities and letting the sediment of hasty decisions sit under the influence 
  of time, we can ensure that our policy decisions are clear, stable, and 
  sustainable, rather than continuously churned up by the stick of over-intervention.

* Key Insights:
  - The principle of Wu-Wei (effortless non-action).
  - Restraint in governance and public policy.
  - Trusting self-regulating natural and social systems.""",

    # 4. Kabir's Death and Flowers
    """--------------------------------------------------------------------------------
Anecdote 4D: Kabir's Shroud of Flowers (Truth / Integrity)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "Truth knows no color." (UPSC 2025)
  - "Values are not what humanity is, but what humanity ought to be." (UPSC 2019)
  - "Your perception of me is a reflection of you; my reaction to you is an awareness of me." (UPSC 2021)

* Narrative:
  In the humid, dust-choked lanes of 15th-century Varanasi, the Bhakti mystic 
  Kabir composed verses that cut clean through the sectarian divide of medieval 
  India. To the Hindu orthodoxy, truth was colored in the saffron of rituals, 
  caste hierarchies, and Sanskrit scriptures. To the Islamic clergy, truth was 
  wrapped in the green of formal dogmas, Arabic texts, and institutionalized 
  power. Kabir rejected both, declaring that the ultimate reality was an unpainted, 
  formless presence—Nirguna. Upon Kabir's death in Maghar, a fierce dispute 
  erupted. The Hindus demanded his body for cremation, claiming him as their 
  guru; the Muslims insisted on burial, claiming him as their Sufi Pir. As the 
  confrontation grew violent, someone drew back the white shroud covering his 
  body. To their absolute bewilderment, the corpse had vanished. In its place 
  lay a heap of fresh, fragrant flowers. Dumbfounded, the two groups divided the 
  flowers. The Hindus cremated their share; the Muslims buried theirs. The colors 
  of their rites remained different, but the entity they sought to possess had 
  transcended beyond both, proving that Truth belongs to no single faction.

* Thesis Pivot (Intro Hook):
  The legend of Kabir's death illustrates that ultimate truth knows no color—it 
  cannot be contained within the sectarian boundaries of religion, language, 
  or culture. In exploring how "truth knows no color," this story reveals that 
  when we attempt to divide reality into opposing factions, we lose the essence 
  of the truth itself. True values exist not in our tribal divisions, but in the 
  syncretic space that unites us.

* Callback & Philosophical Elevation (Conclusion):
  As we navigate a society divided by identity politics and cultural conflicts, 
  we must remember the shroud of flowers at Maghar. We must seek the common ground 
  that lies beneath our different rites and beliefs. By treating truth as a 
  formless, shared reality rather than a colored banner to be fought over, we 
  can build a nation that values unity and mutual respect.

* Key Insights:
  - Truth transcending sectarian divisions.
  - Pluralism and syncretic culture.
  - Nirvana and formless reality (Nirguna).""",

    # 5. George Dantzig
    """--------------------------------------------------------------------------------
Anecdote 3D: George Dantzig and the Impossible Homework (Knowledge / Education)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "What is research, but a blind date with knowledge!" (UPSC 2021)
  - "Thought finds a world and creates one also." (UPSC 2025)
  - "Experience without theory is blind, but theory without experience is mere intellectual play." (Vajiram Test 1)

* Narrative:
  One day, when George Dantzig was a graduate student at the University of 
  California, Berkeley, he arrived late to his statistics class. On the board, 
  the professor had written two very difficult problems. Dantzig thought they 
  were homework questions. He copied them down and went home. The problems 
  looked very hard, so he worked on them for several days. Finally, he solved 
  them and submitted the answers to his professor, Jerzy Neyman. A few weeks 
  later, the professor came to Dantzig’s house very excited. He told him 
  something surprising: those two problems were not homework. They were actually 
  unsolved problems in statistics, which many mathematicians had been trying to 
  solve for years. Without knowing they were “impossible,” Dantzig solved them.

* Thesis Pivot (Intro Hook):
  Dantzig’s breakthrough shows that the perception of what is "impossible" is 
  often a cognitive barrier that prevents discovery. In exploring how "research 
  is a blind date with knowledge," his story reveals that when we approach a 
  problem without the burden of historical failure, we can find solutions that 
  others hesitated to try. Belief and effort are far more powerful than the rules 
  of conventional wisdom.

* Callback & Philosophical Elevation (Conclusion):
  In our educational and policy efforts, we must encourage students to challenge 
  the limits of what is considered possible. We must ensure that our research 
  environments do not crush independent thinking under the weight of established 
  dogma. By letting our students date knowledge blindly—without telling them 
  which problems are unsolvable—we can unlock new paths to progress.

* Key Insights:
  - Breaking through cognitive barriers of impossibility.
  - Intuitive exploration in mathematics and research.
  - Blind dates with unsolved challenges.""",

    # 6. Jeremiah Denton
    """--------------------------------------------------------------------------------
Anecdote 1D: Jeremiah Denton's Morse Code Blinking (Courage / Fortitude)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "Courage to accept and dedication to improve are two keys to success." (UPSC 2019)
  - "In a time of universal deceit, telling the truth is a revolutionary act." (Vajiram Test 3)
  - "A ship in harbour is safe, but that is not what a ship is for." (UPSC 2022)

* Narrative:
  During the Vietnam War, Captain Jeremiah Denton was captured by North Vietnamese 
  forces and kept as a prisoner of war (POW) for several years. He was often 
  tortured and forced to appear in propaganda videos. In 1966, the captors made 
  him appear on television to show the world that American prisoners were being 
  treated well. While answering questions, Denton seemed calm and obedient. But 
  he did something very clever. As he spoke, he blinked his eyes repeatedly. 
  It looked like he was just struggling with the bright lights, but in reality 
  he was using Morse code with his blinking. He blinked the word: T-O-R-T-U-R-E. 
  Through this secret message, he informed the U.S. government that American 
  prisoners in Vietnam were being tortured. This became the first confirmed 
  evidence of the mistreatment of American POWs in North Vietnam.

* Thesis Pivot (Intro Hook):
  Jeremiah Denton’s blinking Morse code is a powerful example of moral courage 
  and presence of mind under extreme pressure. In discussing how "telling the 
  truth in a time of universal deceit is a revolutionary act," his story shows 
  that even when physically bound and silenced, an individual can find creative, 
  subtle ways to stand by their truth.

* Callback & Philosophical Elevation (Conclusion):
  Denton's silent blinks remind us that our integrity cannot be imprisoned unless 
  we choose to surrender it. When we face environments of censorship or systemic 
  dishonesty, we must use our intelligence to find ways to speak the truth. By 
  maintaining our moral alignment even under coercion, we keep the light of 
  truth burning.

* Key Insights:
  - Presence of mind under physical capture and torture.
  - Subtle resistance against institutional deceit.
  - Communicating truth via standard code in creative mediums.""",

    # 7. Ernest Shackleton
    """--------------------------------------------------------------------------------
Anecdote 1E: Ernest Shackleton's Rescue Mission (Courage / Fortitude)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "Character of an institution is reflected in its leader." (UPSC 2015)
  - "He who has a why to live for can bear almost any how." (Vajiram Test 3)
  - "Best lessons are learnt through bitter experiences." (UPSC 2025)

* Narrative:
  In 1915, British explorer Ernest Shackleton set out on an ambitious expedition 
  to cross Antarctica. His ship, Endurance, however, became trapped in thick 
  Antarctic ice. After months of pressure from the ice, the ship was eventually 
  crushed and sank, leaving Shackleton and his crew stranded in one of the 
  harshest environments on Earth. With freezing temperatures, limited food, and 
  no chance of immediate rescue, the situation looked hopeless. At that moment, 
  Shackleton made a remarkable decision. He abandoned the mission of exploration 
  and announced a new goal to his crew: "The expedition is over. Now our mission 
  is to get everyone home alive." For months, Shackleton kept the crew motivated 
  and united. He carefully rationed food, maintained discipline, and constantly 
  lifted the morale of his men. Even when they had to survive on drifting ice 
  and later make a dangerous journey across the stormy Southern Ocean in small 
  boats, Shackleton never allowed despair to take over. After nearly two years 
  of struggle, he successfully organized a rescue mission. Remarkably, every 
  single member of the expedition survived.

* Thesis Pivot (Intro Hook):
  Shackleton's leadership during the Endurance crisis shows that a leader's 
  character is tested not in moments of victory, but in how they manage failure 
  and prioritize their team. In exploring how "he who has a why to live for 
  can bear almost any how," his decision to shift focus from ambition to survival 
  gave his men a collective purpose that kept hope alive in the coldest abyss.

* Callback & Philosophical Elevation (Conclusion):
  In our modern institutions and enterprises, leadership must prioritize human 
  life and collective well-being over raw target acquisition. By maintaining 
  morale, discipline, and unity during crises, leaders can guide their teams 
  through the most hostile environments, proving that a leader's true legacy 
  is the safety and integrity of their people.

* Key Insights:
  - Pivoting objectives under critical constraints.
  - Team survival as the ultimate success measure.
  - Emotional intelligence in high-stress environments.""",

    # 8. Bruce Lee
    """--------------------------------------------------------------------------------
Anecdote 1F: Bruce Lee's "Be Like Water" Recovery (Courage / Fortitude)
--------------------------------------------------------------------------------
* Mapped Essay Prompts:
  - "That which does not kill us makes us stronger." (Vajiram Test 2)
  - "A ship in harbour is safe, but that is not what a ship is for." (UPSC 2022)
  - "Courage to accept and dedication to improve are two keys to success." (UPSC 2019)

* Narrative:
  In the early 1970s, at the peak of his physical prowess, Bruce Lee suffered 
  a severe back injury during a training session. Doctors told him he might 
  never practice martial arts again. For someone whose identity revolved around 
  movement, strength, and discipline, this was devastating. Instead of giving 
  up, Bruce Lee adapted. Confined to bed for months, he began writing extensively—
  refining his philosophy of life and martial arts. It was during this period 
  that he deeply articulated his famous idea: "Be like water." Water, he believed, 
  does not resist obstacles—it flows around them, adjusts, reshapes, yet remains 
  powerful. Against all odds, Bruce Lee not only recovered but returned stronger—
  physically and mentally. He went on to revolutionize martial arts and global 
  cinema.

* Thesis Pivot (Intro Hook):
  Bruce Lee’s recovery reveals that resilience is not merely physical toughness, 
  but the mental capacity to adapt to constraints. In discussing the "courage to 
  accept and dedication to improve," his bedridden months show that when our 
  physical paths are blocked, we must reshape our efforts, finding new avenues 
  for growth rather than giving up.

* Callback & Philosophical Elevation (Conclusion):
  As we encounter the inevitable obstacles of our lives, we must strive to be 
  like water. Instead of breaking against the barriers of adversity, we must 
  flow around them, using constraints as opportunities to refine our minds and 
  characters, ensuring that we return stronger and more adaptable.

* Key Insights:
  - Physical recovery through intellectual and philosophical adaptation.
  - Metaphor of water representing flexibility and power.
  - Turning complete somatic breakdown into cognitive breakthrough."""
]

# Append the text entries to anecdotes.txt right before the final line of equal signs
# Let's search for "================================================================================" at the end of the file.
if "Ramanujan's Intuitive Mock Theta Functions" not in txt_content:
    divider = "================================================================================"
    parts = txt_content.rsplit(divider, 1)
    if len(parts) == 2:
        new_txt_content = parts[0] + "\\n\\n" + "\\n\\n".join(new_txt_entries) + "\\n\\n" + divider + parts[1]
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(new_txt_content)
        print("Updated anecdotes.txt successfully!")
else:
    print("anecdotes.txt already contains the new cards.")

# Now update anecdotes_print.html if it exists
import os
if os.path.exists(print_path):
    with open(print_path, 'r', encoding='utf-8') as f:
        print_content = f.read()

    # Define print summary boxes to add
    # We want to add these boxes under the respective theme-blocks.
    # The themes are:
    # 1. Courage & Fortitude (We want to add 1D: Denton, 1E: Shackleton, 1F: Bruce Lee)
    # 2. Wisdom & Time (We want to add 2D: Lao Tzu)
    # 3. Knowledge & Education (We want to add 3D: George Dantzig)
    # 4. Truth & Integrity (We want to add 4D: Kabir Shroud of Flowers)
    # 5. Visionary Decision-Making (We want to add 5D: Ramanujan)
    # 12. Art, Inspiration & the Human Spirit (We want to add 12D: Gitanjali)

    # Since grid layout is repeat(3, 1fr) for 3 anecdotes, if we add more, we should adapt the grids
    # Or we can just insert them under the list. For print.html, let's keep them in the grid, which will auto-wrap to next row.
    # Let's write the print summary replacements. We'll search for the anecdotes-grid closing </div> of each theme and insert them.
    # Let's write a python search and replace for print_content.

    # For Theme 1: Courage (add Denton, Shackleton, Bruce Lee)
    theme1_target = """        <div class="anecdote-box">
          <div class="anec-title">1C. Malala Yousafzai</div>
          <div class="section-label">Narrative</div>
          In Swat Valley, 11-year-old Malala blogged for female education under Taliban rule. In 2012, she was shot in the head on her school bus. Survived and declared at the UN: "They thought bullets would silence us, but out of that silence came thousands of voices."
          <div class="section-label">Intro Hook</div>
          The search for dignity and knowledge cannot be crushed by raw violence; a clear purpose transforms trauma into historic triumph.
          <div class="section-label">Outro Callback</div>
          A bullet could not silence her, proving that one child, one teacher, one pen, and one book can change the world.
          <div class="insights-list">#FemaleEducation #OvercomingTerror</div>
        </div>"""

    theme1_replace = theme1_target + """
        <div class="anecdote-box">
          <div class="anec-title">1D. Jeremiah Denton</div>
          <div class="section-label">Narrative</div>
          Captured as a Vietnam War POW, Denton was forced to appear on television. He calmly blinked Morse code "T-O-R-T-U-R-E" to warn the US government, choosing subtle resistance under extreme threat.
          <div class="section-label">Intro Hook</div>
          Telling the truth in a time of universal deceit remains a revolutionary act, requiring presence of mind under pressure.
          <div class="section-label">Outro Callback</div>
          Denton's blinks show that integrity cannot be captured; we must use our intellect to stand by our values under coercion.
          <div class="insights-list">#POWResistance #MorseCode</div>
        </div>
        <div class="anecdote-box">
          <div class="anec-title">1E. Ernest Shackleton</div>
          <div class="section-label">Narrative</div>
          In 1915, Shackleton's ship Endurance was crushed by Antarctic ice. He pivoted from exploration to survival: "Now our mission is to get everyone home alive." After 2 years of freezing survival, all crew members were rescued.
          <div class="section-label">Intro Hook</div>
          Leadership is tested not in target acquisition, but in crisis management and prioritizing human lives over ambition.
          <div class="section-label">Outro Callback</div>
          Shackleton's return proves that team solidarity and morale can guide groups through the most hostile environments.
          <div class="insights-list">#Endurance #CrisisLeadership</div>
        </div>
        <div class="anecdote-box">
          <div class="anec-title">1F. Bruce Lee</div>
          <div class="section-label">Narrative</div>
          Suffering a crippling back injury in 1970, Bruce Lee was told he would never fight again. Bedridden, he wrote his philosophy of "Be like water"—flexible, adaptable, flowing around obstacles yet remaining powerful—recovering fully.
          <div class="section-label">Intro Hook</div>
          Resilience is somatic and mental flexibility. When a path is blocked, courage accepts and reframes the focus.
          <div class="section-label">Outro Callback</div>
          By flowing like water, we adapt to constraints, using life's blockades to refine our inner strength.
          <div class="insights-list">#BeLikeWater #OvercomingInjury</div>
        </div>"""

    # For Theme 2: Wisdom (add Lao Tzu)
    theme2_target = """        <div class="anecdote-box">
          <div class="anec-title">2C. Jadav Payeng's Forest</div>
          <div class="section-label">Narrative</div>
          In 1979, seeing heat-scorched snakes on a barren sandbar, 16-year-old Jadav began planting a tree daily in Assam. Today, it is the 1,300-acre Molai Forest, home to rhinos, tigers, and elephants, built entirely through one man's quiet consistency.
          <div class="section-label">Intro Hook</div>
          Ecological degradation cannot be solved by instant decrees, but by persistent, quiet stewardship over decades.
          <div class="section-label">Outro Callback</div>
          Payeng's forest stands as a beacon, reminding us that time, partnered with consistency, can turn a desert back into a cradle of life.
          <div class="insights-list">#EcoStewardship #Consistency</div>
        </div>"""

    theme2_replace = theme2_target + """
        <div class="anecdote-box">
          <div class="anec-title">2D. Lao Tzu's Stream</div>
          <div class="section-label">Narrative</div>
          During ancient China's Warring States, Lao Tzu compared hyperactive governance to stirring muddy water with a stick. He showed that letting a churned stream sit in silence allows gravity to pull down the mud, clearing it naturally.
          <div class="section-label">Intro Hook</div>
          Complex problems are often best solved through patient, deliberate non-action (Wu-Wei) rather than restless, heavy intervention.
          <div class="section-label">Outro Callback</div>
          By allowing systems to settle under time, public policy can avoid creating noise and let natural equilibrium restore itself.
          <div class="insights-list">#WuWei #PublicRestraint</div>
        </div>"""

    # For Theme 3: Knowledge (add George Dantzig)
    theme3_target = """        <div class="anecdote-box">
          <div class="anec-title">3C. Helen Keller's Water</div>
          <div class="section-label">Narrative</div>
          Deaf-blind and prone to tantrums, Helen Keller's world changed when Anne Sullivan put her hand under a cold water pump and spelled W-A-T-E-R on her other hand, connecting tactile sensation to language and unlocking her intellect.
          <div class="section-label">Intro Hook</div>
          Education is not the mechanical memorization of abstract facts, but the empathetic awakening of the soul to meaning.
          <div class="section-label">Outro Callback</div>
          We must design learning systems that act as water pumps, bringing light and agency to the dark and silent spaces of the mind.
          <div class="insights-list">#OvercomingLimits #EmpatheticTeaching</div>
        </div>"""

    theme3_replace = theme3_target + """
        <div class="anecdote-box">
          <div class="anec-title">3D. George Dantzig</div>
          <div class="section-label">Narrative</div>
          Late to a Berkeley statistics class, graduate student George Dantzig copied down two math problems on the blackboard, assuming they were homework. He worked on them for days and solved them, unaware they were famous "unsolved" statistics equations.
          <div class="section-label">Intro Hook</div>
          The perception of impossibility is a cognitive cage. Approaching research without the history of failure unlocks hidden answers.
          <div class="section-label">Outro Callback</div>
          By letting our students date knowledge blindly—unburdened by what is "impossible"—we create rooms for revolutionary solutions.
          <div class="insights-list">#GeorgeDantzig #NoBarriers</div>
        </div>"""

    # For Theme 4: Truth (add Kabir death flowers)
    theme4_target = """        <div class="anecdote-box">
          <div class="anec-title">4C. Dr. Li Wenliang's Warning</div>
          <div class="section-label">Narrative</div>
          In December 2019, Dr. Li warned colleagues about a SARS-like virus in Wuhan. Silenced by police and forced to sign an admonishment for "making false comments," he returned to treat patients, caught COVID-19, and died.
          <div class="section-label">Intro Hook</div>
          When state organs prioritize public relations over objective facts, they turn administrative deceit into human tragedy.
          <div class="section-label">Outro Callback</div>
          Dr. Li's warning outlived the police admonishment, showing that administrative suppression cannot contain objective truths.
          <div class="insights-list">#Whistleblowing #PublicHealthEthics</div>
        </div>"""

    theme4_replace = theme4_target + """
        <div class="anecdote-box">
          <div class="anec-title">4D. Kabir's Shroud</div>
          <div class="section-label">Narrative</div>
          On Kabir's death, Hindus and Muslims fought to claim his body for cremation or burial. When they drew back the shroud, they found only a heap of flowers. They divided the flowers, continuing their separate rites for a formless reality.
          <div class="section-label">Intro Hook</div>
          Ultimate truth knows no sectarian color; attempting to parcel it into factional boxes destroys its formless essence.
          <div class="section-label">Outro Callback</div>
          Kabir's shroud teaches us to look beyond sectarian banners, finding unity in values rather than divisions in dogmatic colors.
          <div class="insights-list">#BhaktiPluralism #NirgunaTruth</div>
        </div>"""

    # For Theme 5: Decision Making (add Ramanujan)
    theme5_target = """        <div class="anecdote-box">
          <div class="anec-title">5C. Chanakya's Pancake</div>
          <div class="section-label">Narrative</div>
          After failing to defeat the Nandas by attacking the capital directly, Chanakya saw a mother scold her child for burning fingers by eating a pancake from the center. He intuitively realized they must conquer the borders first.
          <div class="section-label">Intro Hook</div>
          Strategic success requires learning from simple observations and modifying military logic with intuitive, real-world context.
          <div class="section-label">Outro Callback</div>
          By looking to the periphery (the edge of the pancake), Chanakya re-engineered his logic to build the Mauryan Empire.
          <div class="insights-list">#Statecraft #GrassrootsFeedback</div>
        </div>"""

    theme5_replace = theme5_target + """
        <div class="anecdote-box">
          <div class="anec-title">5D. Ramanujan's Slate</div>
          <div class="section-label">Narrative</div>
          Armed only with slate and chalk in Kumbakonam, Ramanujan discovered complex math, claiming equations were written on his tongue in dreams. On his deathbed, he wrote "Mock Theta Functions" that physicists only decoded a century later to calculate black hole entropy.
          <div class="section-label">Intro Hook</div>
          Intuitive thought can outrun formal analytical logic by decades, creating abstract universes that eventually decode reality.
          <div class="section-label">Outro Callback</div>
          Ramanujan proves that we must trust intuitive flashes, combining the music of reason with the logic of formal proof.
          <div class="insights-list">#Ramanujan #BlackHoleMock</div>
        </div>"""

    # For Theme 12: Art & Spirit (add Gitanjali)
    theme12_target = """        <div class="anecdote-box">
          <div class="anec-title">12C. Bismillah Khan in Varanasi</div>
          <div class="section-label">Narrative</div>
          During Partition in 1947, shehnai maestro Ustad Bismillah Khan refused to migrate to Pakistan, declaring his soul belonged to the Ganga and Kashi Vishwanath temple courtyard, representing Varanasi's syncretic culture.
          <div class="section-label">Intro Hook</div>
          Cultural identity and artistic connection are deeper than political borders, weaving communities around shared plural heritages.
          <div class="section-label">Outro Callback</div>
          Bismillah Khan's music reminds us to celebrate our syncretic traditions, keeping the song of syncretic unity alive.
          <div class="insights-list">#GangaJamuniTehzeeb #VaranasiShehnai</div>
        </div>"""

    theme12_replace = theme12_target + """
        <div class="anecdote-box">
          <div class="anec-title">12D. Tagore's Crucible</div>
          <div class="section-label">Narrative</div>
          Between 1902 and 1907, Tagore lost his wife, daughter, and youngest son in quick succession. Amidst deep grief, he wrote the poems of Gitanjali, transforming personal bereavement into a universal Nobel Prize-winning spiritual offering.
          <div class="section-label">Intro Hook</div>
          Deep human wisdom is forged in the shadows of adversity; poetry sublimates personal raw pain into global empathy.
          <div class="section-label">Outro Callback</div>
          Tagore's crucible shows that finding a purpose (a "why") in grief allows the creative spirit to legislate moral hope.
          <div class="insights-list">#Gitanjali #AdversitySublimation</div>
        </div>"""

    if "Ramanujan's Slate" not in print_content:
        print_content = print_content.replace(theme1_target, theme1_replace)
        print_content = print_content.replace(theme2_target, theme2_replace)
        print_content = print_content.replace(theme3_target, theme3_replace)
        print_content = print_content.replace(theme4_target, theme4_replace)
        print_content = print_content.replace(theme5_target, theme5_replace)
        print_content = print_content.replace(theme12_target, theme12_replace)
        
        with open(print_path, 'w', encoding='utf-8') as f:
            f.write(print_content)
        print("Updated anecdotes_print.html successfully!")
    else:
        print("anecdotes_print.html already contains the new cards.")

print("All updates completed successfully!")
