Promise.all([
  fetch('../../data/categories.json').then(r => r.json()),
  fetch('../../data/news.json').then(r => r.json()),
  fetch('../../data/stats.json').then(r => r.json())
]).then(([categories, news, stats]) => {
  console.log('AION NEXUS data ok', { categories: categories.length, news: news.length, stats });
}).catch(err => console.error('AION NEXUS data load failed', err));
