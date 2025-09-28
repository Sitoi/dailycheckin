import { Cards, Card } from 'nextra/components'
import type { ReactNode } from 'react'

interface CardItem {
  title: string;
  href: string;
  icon?: ReactNode;
  children?: ReactNode;
}

interface CardListProps {
  cards: CardItem[];
}

const defaultCards: CardItem[] = [
  { title: 'AcFun', href: '/settings/acfun' },
  { title: '奥拉星', href: '/settings/aolaxing' },
  { title: '阿里云盘', href: '/settings/aliyun' },
  { title: 'Baidu 站点提交', href: '/settings/baidu' },
  { title: '百度网盘会员', href: '/settings/baiduwp' },
  { title: 'Bilibili', href: '/settings/bilibili' },
  { title: '恩山无线论坛', href: '/settings/enshan' },
  { title: 'i茅台', href: '/settings/imaotai' },
  { title: '爱奇艺', href: '/settings/iqiyi' },
  { title: '全民 K 歌', href: '/settings/kgqq' },
  { title: '小米运动', href: '/settings/mimotion' },
  { title: '什么值得买', href: '/settings/smzdm' },
  { title: '百度贴吧', href: '/settings/tieba' },
  { title: 'V2EX', href: '/settings/v2ex' },
  { title: '有道云笔记', href: '/settings/youdao' },
]

export default function CardList({ cards = defaultCards }: CardListProps) {
  return (
    <Cards>
      {cards.map((item) => (
        <Card key={item.href} title={item.title} href={item.href} icon={item.icon}>
          {item.children}
        </Card>
      ))}
    </Cards>
  );
}
