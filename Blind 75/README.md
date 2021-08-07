<h1>Blind 75</h1>
  <a href="https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions">Leetcode link to the post.</a>
  <h2>Array</h2>
    <ul>
      <li><a href="Programs/Two Sum.py">Two Sum</a> 
        <p>Approach: Solved using hash table, you can even solve this using 2 pointer approach where you'd have to sort the array, but then you won't be able to return index. </p>
      </li>
      <li> Three Sum
      <ol>
        <li><a href="Programs/Three Sum - ForLoops.py">Solved using 3 for loops</a>: Time complexity O(n^3), Leetcode time limit exceeded. </li>
        <li><a href="Programs/Three Sum - Recursion.py">Solved using Recursion</a>: Leetcode time limit exceeded. </li>
        <li><a href="Programs/Three Sum - 2 Pointer.py">Solved using 2 pointers and a for loop</a>: Time Complexity O(n^2), Leetcode accepted.</li>
      </ol>
      </li>
      <li> <a href="Programs/Container With Most Water.py">Container With Most Water</a>
        <p> Approach: 2 Pointers to keep track of left and right poles.
        </p>
      </li>
    </ul>
  <h2>Graph</h2>
    <ul>
      <li><a href="Programs/Course Schedule.py">Course Schedule</a>
        <p>Approach: Used BFS topological sort. Understood the approach from <a href="https://leetcode.com/discuss/general-discussion/1078072/introduction-to-topological-sort">this article</a>.<br/>
          The following pseudo code helped. <br/>
          <pre><code>
            L = Empty list that will contain the sorted elements <br/>
            S = Set of all nodes with no incoming edge <br/>
            <br/>
              While S is non-empty do: <br/>
                &ensp; remove a node n from S <br/>
                &ensp; add n to tail of L <br/>
                &ensp; for each node m with an edge e from n to m do <br/>
                  &ensp; &ensp; remove edge e from the graph <br/>
                  &ensp; &ensp; if m has no other incoming edges then <br/>
                    &ensp; &ensp; &ensp; insert m into S <br/>
              <br/>
              if graph has edges then <br/>
                &ensp; return error   (graph has at least one cycle) <br/>
              else <br/>
                &ensp; return L   (a topologically sorted order) <br/>
          </code></pre>
        </p>
      </li>
    </ul>
  <h2>String</h2>
    <ul>
      <li><a href="Programs/Longest%20Substring%20Without%20Repeating%20Characters.py">Longest Substring Without Repeating Characters</a> <br/>
        <p>Approach: We use sliding window for this one. Use hash table to keep track of the letters in the window.</p>
      </li>
      <li><a href="Programs/Longest Repeating Character Replacement.py">Longest Repeating Character Replacement</a> 
        <p>Approach: Following formula used <br/>
          (length of substring - number of times of the maximum occurring character in the substring) <= k  
        </p>
      </li>
    </ul>
  <h2>Tree</h2>
    <ul>
      <li><a href="Programs/Implement Trie.py">Implement Trie (Prefix Tree)</a>
        <p>Thoughts: You can also use this approach to serialise and de-serialise an n-ary tree.</p>
      </li>
    </ul>





