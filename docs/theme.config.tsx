import { useRouter } from 'next/router'
import { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: <span className="nx-text-3xl nx-font-bold">DailyCheckin</span>,
  project: {
    link: 'https://github.com/Sitoi/dailycheckin',
  },
  chat: {
    link: 'https://t.me/dailycheckin',
    icon: (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 256 256"
      >
        <defs>
          <linearGradient
            id="IconifyId18cfc9cea1e90987a0"
            x1="50%"
            x2="50%"
            y1="0%"
            y2="100%"
          >
            <stop
              offset="0%"
              stopColor="#2AABEE"
            />
            <stop
              offset="100%"
              stopColor="#229ED9"
            />
          </linearGradient>
        </defs>
        <path
          fill="url(#IconifyId18cfc9cea1e90987a0)"
          d="M128 0C94.06 0 61.48 13.494 37.5 37.49A128.038 128.038 0 0 0 0 128c0 33.934 13.5 66.514 37.5 90.51C61.48 242.506 94.06 256 128 256s66.52-13.494 90.5-37.49c24-23.996 37.5-56.576 37.5-90.51c0-33.934-13.5-66.514-37.5-90.51C194.52 13.494 161.94 0 128 0"
        />
        <path
          fill="#FFF"
          d="M57.94 126.648c37.32-16.256 62.2-26.974 74.64-32.152c35.56-14.786 42.94-17.354 47.76-17.441c1.06-.017 3.42.245 4.96 1.49c1.28 1.05 1.64 2.47 1.82 3.467c.16.996.38 3.266.2 5.038c-1.92 20.24-10.26 69.356-14.5 92.026c-1.78 9.592-5.32 12.808-8.74 13.122c-7.44.684-13.08-4.912-20.28-9.63c-11.26-7.386-17.62-11.982-28.56-19.188c-12.64-8.328-4.44-12.906 2.76-20.386c1.88-1.958 34.64-31.748 35.26-34.45c.08-.338.16-1.598-.6-2.262c-.74-.666-1.84-.438-2.64-.258c-1.14.256-19.12 12.152-54 35.686c-5.1 3.508-9.72 5.218-13.88 5.128c-4.56-.098-13.36-2.584-19.9-4.708c-8-2.606-14.38-3.984-13.82-8.41c.28-2.304 3.46-4.662 9.52-7.072"
        />
      </svg>
    ),
  },
  head: (
    <>
      <script
        async
        src="https://umami.sitoi.cn/script.js"
        data-website-id="93cd32e8-03fb-4896-9420-6d9bff2d2359"
      ></script>
    </>
  ),
  footer: {
    text: 'DailyCheckin Docs © 2024',
  },
  docsRepositoryBase: 'https://github.com/Sitoi/dailycheckin',
  feedback: {
    content: '',
  },
  editLink: {
    text: '',
  },
  useNextSeoProps() {
    const { asPath } = useRouter()
    if (asPath !== '/') {
      return {
        titleTemplate: '%s – DailyCheckIn',
      }
    }
  },
  banner: {
    key: '2025.1.7-release',
    text: (
      <a
        href="/dailycheckin/history/2025-01-07/"
        target="_blank"
      >
        🎉 DailyCheckIn 2025.1.7 is released. Read more →
      </a>
    ),
  },
}

export default config
