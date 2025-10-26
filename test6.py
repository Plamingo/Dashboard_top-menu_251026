import streamlit as st
import streamlit.components.v1 as components


css = '''
<style>
@font-face {
	font-family: "GmarketSansMedium";
	src: url("https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff")
		format("woff");
	font-weight: normal;
	font-style: normal;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "GmarketSansMedium";
  padding: 20px;
}

.container{
  max-width: 1200px;
  margin-inline: auto;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  overflow: hidden;
}

h1 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  text-align: center;
  font-size: 2rem;
  margin-bottom: 0;
}

.table-container{
  overflow-x: auto;
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 30px;
  font-size: 14px;
}

th,td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
  vertical-align: top;
}

th {
  background-color: #f8f9fa;
  font-weight: bold;
  color: #495057;
  text-align: center;
}

.category {
  background-color: #e9ecef;
  font-weight: bold;
  text-align: center;
  width: 100px;
}

.inline-group {
  background-color: #e3f2fd;
}

.block-group {
  background-color: #f3e5f5;
}

.none-group {
  background-color: #ffebee;
}

.examples {
  padding: 20px;
  background-color: #f8f9fa;
}

.examples h2 {
  color: #495057;
  margin-bottom: 15px;
  font-size: 1.5rem;
}

.example-list {
  list-style: none;
  padding-left: 0;
}

.example-list li {
  margin-bottom: 8px;
  padding: 8px 12px;
  background: white;
  border-left: 4px solid #667eea;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.highlight {
  background-color: #fff3cd;
  padding: 2px 4px;
  border-radius: 3px;
  font-weight: bold;
}

@media (max-width: 768px) {
  body {
    padding: 10px;
  }
  h1 {
    font-size: 1.5rem;
    padding: 15px;
  }
  .table-container {
    padding: 10px;
  }
  table{
    font-size: 12px;
  }
  th,td {
    padding: 8px;
  }
  .category {
    width: 60px;
  }
  examples {
    padding: 15px;
  }
}
@media (max-width: 480px) {
  h1 {
    font-size: 1.3rem;
    padding: 12px;
  }
  table {
    font-size: 11px;
  }
  th,td {
    padding: 6px;
  }
  .example-list li {
    padding: 6px 8px;
    font-size: 13px;
  }
}
</style>'''

html = '''<div class="container">
  <h1>display 속성정리</h1>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>종류</th>
          <th class="inline-group">inline-block, inline, inline-flex</th>
          <th class="block-group">block, flex</th>
          <th class="none-group">none</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="category">너비</td>
          <td class="inline-group">너비 미설정 = 최소화</td>
          <td class="block-group">너비 미설정 = 최대화</td>
          <td class="none-group">없어진다.</td>
        </tr>
        <tr>
          <td class="category">높이</td>
          <td class="inline-group">높이 미설정 = 최소화</td>
          <td class="block-group">높이 미설정 = 최소화</td>
          <td class="none-group">없어진다.</td>
        </tr>
        <tr>
          <td class="category">본질</td>
          <td class="inline-group">글자화</td>
          <td class="block-group">블록화</td>
          <td class="none-group">-</td>
        </tr>
        <tr>
          <td class="category">line 사용</td>
          <td class="inline-group">한 줄에 최대한 여러개 나온다</td>
          <td class="block-group">한 줄을 무조건 혼자 쓴다</td>
          <td class="none-group">-</td>
        </tr>
        <tr>
          <td class="category">정렬</td>
          <td class="inline-group">부모의 text-align에 의해 정렬</td>
          <td class="block-group">스스로 margin-left, margin-right 사용하여 정렬</td>
          <td class="none-group">-</td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <div class="examples">
    <h2>예외</h2>
    <ul class="example-list">
      <li><span class="highlight">a, span</span>엘리먼트는 기본적으로 display가 <span class="highlight">inline</span>이다.</li>
      <li><span class="highlight">img</span>엘리먼트는 기본적으로 display가 <span class="highlight">inline-block</span>이다.</li>
      <li><span class="highlight">inline</span>요소에는 width, height, margin, padding 속성이 제대로 적용되지 않는다.</li>
    </ul>
  </div>
</div>'''

st.write('test5')
components.html(css+html,height=800)