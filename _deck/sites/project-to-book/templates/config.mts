import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '{{PROJECT_TITLE}}',
  description: '{{PROJECT_DESCRIPTION}}',
  srcDir: './docs',
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Interview', link: '/interview/' },
      { text: 'Source', link: '/source/' },
      { text: 'Practice', link: '/practice/' }
    ],
    sidebar: {
      '/interview/': [
        {
          text: 'Interview Questions',
          items: [
            {{INTERVIEW_SIDEBAR_ITEMS}}
          ]
        }
      ],
      '/source/': [
        {
          text: 'Source Walkthrough',
          items: [
            {{SOURCE_SIDEBAR_ITEMS}}
          ]
        }
      ],
      '/practice/': [
        {
          text: 'Practice',
          items: [
            { text: 'Overview', link: '/practice/' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: '{{GITHUB_URL}}' }
    ]
  }
})
