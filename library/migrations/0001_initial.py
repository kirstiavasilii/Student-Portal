# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import library.models
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='название', max_length=150)),
                ('author', models.CharField(verbose_name='автор(ы)', max_length=50)),
                ('imprint_date', models.IntegerField(choices=[(2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896), (1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890), (1889, 1889), (1888, 1888), (1887, 1887), (1886, 1886), (1885, 1885), (1884, 1884), (1883, 1883), (1882, 1882), (1881, 1881), (1880, 1880), (1879, 1879), (1878, 1878), (1877, 1877), (1876, 1876), (1875, 1875), (1874, 1874), (1873, 1873), (1872, 1872), (1871, 1871), (1870, 1870), (1869, 1869), (1868, 1868), (1867, 1867), (1866, 1866), (1865, 1865), (1864, 1864), (1863, 1863), (1862, 1862), (1861, 1861), (1860, 1860), (1859, 1859), (1858, 1858), (1857, 1857), (1856, 1856), (1855, 1855), (1854, 1854), (1853, 1853), (1852, 1852), (1851, 1851), (1850, 1850), (1849, 1849), (1848, 1848), (1847, 1847), (1846, 1846), (1845, 1845), (1844, 1844), (1843, 1843), (1842, 1842), (1841, 1841), (1840, 1840), (1839, 1839), (1838, 1838), (1837, 1837), (1836, 1836), (1835, 1835), (1834, 1834), (1833, 1833), (1832, 1832), (1831, 1831), (1830, 1830), (1829, 1829), (1828, 1828), (1827, 1827), (1826, 1826), (1825, 1825), (1824, 1824), (1823, 1823), (1822, 1822), (1821, 1821), (1820, 1820), (1819, 1819), (1818, 1818), (1817, 1817), (1816, 1816), (1815, 1815), (1814, 1814), (1813, 1813), (1812, 1812), (1811, 1811), (1810, 1810), (1809, 1809), (1808, 1808), (1807, 1807), (1806, 1806), (1805, 1805), (1804, 1804), (1803, 1803), (1802, 1802), (1801, 1801), (1800, 1800), (1799, 1799), (1798, 1798), (1797, 1797), (1796, 1796), (1795, 1795), (1794, 1794), (1793, 1793), (1792, 1792), (1791, 1791), (1790, 1790), (1789, 1789), (1788, 1788), (1787, 1787), (1786, 1786), (1785, 1785), (1784, 1784), (1783, 1783), (1782, 1782), (1781, 1781), (1780, 1780), (1779, 1779), (1778, 1778), (1777, 1777), (1776, 1776), (1775, 1775), (1774, 1774), (1773, 1773), (1772, 1772), (1771, 1771), (1770, 1770), (1769, 1769), (1768, 1768), (1767, 1767), (1766, 1766), (1765, 1765), (1764, 1764), (1763, 1763), (1762, 1762), (1761, 1761), (1760, 1760), (1759, 1759), (1758, 1758), (1757, 1757), (1756, 1756), (1755, 1755), (1754, 1754), (1753, 1753), (1752, 1752), (1751, 1751), (1750, 1750), (1749, 1749), (1748, 1748), (1747, 1747), (1746, 1746), (1745, 1745), (1744, 1744), (1743, 1743), (1742, 1742), (1741, 1741), (1740, 1740), (1739, 1739), (1738, 1738), (1737, 1737), (1736, 1736), (1735, 1735), (1734, 1734), (1733, 1733), (1732, 1732), (1731, 1731), (1730, 1730), (1729, 1729), (1728, 1728), (1727, 1727), (1726, 1726), (1725, 1725), (1724, 1724), (1723, 1723), (1722, 1722), (1721, 1721), (1720, 1720), (1719, 1719), (1718, 1718), (1717, 1717), (1716, 1716), (1715, 1715), (1714, 1714), (1713, 1713), (1712, 1712), (1711, 1711), (1710, 1710), (1709, 1709), (1708, 1708), (1707, 1707), (1706, 1706), (1705, 1705), (1704, 1704), (1703, 1703), (1702, 1702), (1701, 1701), (1700, 1700), (1699, 1699), (1698, 1698), (1697, 1697), (1696, 1696), (1695, 1695), (1694, 1694), (1693, 1693), (1692, 1692), (1691, 1691), (1690, 1690), (1689, 1689), (1688, 1688), (1687, 1687), (1686, 1686), (1685, 1685), (1684, 1684), (1683, 1683), (1682, 1682), (1681, 1681), (1680, 1680), (1679, 1679), (1678, 1678), (1677, 1677), (1676, 1676), (1675, 1675), (1674, 1674), (1673, 1673), (1672, 1672), (1671, 1671), (1670, 1670), (1669, 1669), (1668, 1668), (1667, 1667), (1666, 1666), (1665, 1665), (1664, 1664), (1663, 1663), (1662, 1662), (1661, 1661), (1660, 1660), (1659, 1659), (1658, 1658), (1657, 1657), (1656, 1656), (1655, 1655), (1654, 1654), (1653, 1653), (1652, 1652), (1651, 1651), (1650, 1650), (1649, 1649), (1648, 1648), (1647, 1647), (1646, 1646), (1645, 1645), (1644, 1644), (1643, 1643), (1642, 1642), (1641, 1641), (1640, 1640), (1639, 1639), (1638, 1638), (1637, 1637), (1636, 1636), (1635, 1635), (1634, 1634), (1633, 1633), (1632, 1632), (1631, 1631), (1630, 1630), (1629, 1629), (1628, 1628), (1627, 1627), (1626, 1626), (1625, 1625), (1624, 1624), (1623, 1623), (1622, 1622), (1621, 1621), (1620, 1620), (1619, 1619), (1618, 1618), (1617, 1617), (1616, 1616), (1615, 1615), (1614, 1614), (1613, 1613), (1612, 1612), (1611, 1611), (1610, 1610), (1609, 1609), (1608, 1608), (1607, 1607), (1606, 1606), (1605, 1605), (1604, 1604), (1603, 1603), (1602, 1602), (1601, 1601), (1600, 1600), (1599, 1599), (1598, 1598), (1597, 1597), (1596, 1596), (1595, 1595), (1594, 1594), (1593, 1593), (1592, 1592), (1591, 1591), (1590, 1590), (1589, 1589), (1588, 1588), (1587, 1587), (1586, 1586), (1585, 1585), (1584, 1584), (1583, 1583), (1582, 1582), (1581, 1581), (1580, 1580), (1579, 1579), (1578, 1578), (1577, 1577), (1576, 1576), (1575, 1575), (1574, 1574), (1573, 1573), (1572, 1572), (1571, 1571), (1570, 1570), (1569, 1569), (1568, 1568), (1567, 1567), (1566, 1566), (1565, 1565), (1564, 1564), (1563, 1563), (1562, 1562), (1561, 1561), (1560, 1560), (1559, 1559), (1558, 1558), (1557, 1557), (1556, 1556), (1555, 1555), (1554, 1554), (1553, 1553), (1552, 1552), (1551, 1551), (1550, 1550), (1549, 1549), (1548, 1548), (1547, 1547), (1546, 1546), (1545, 1545), (1544, 1544), (1543, 1543), (1542, 1542), (1541, 1541), (1540, 1540), (1539, 1539), (1538, 1538), (1537, 1537), (1536, 1536), (1535, 1535), (1534, 1534), (1533, 1533), (1532, 1532), (1531, 1531), (1530, 1530), (1529, 1529), (1528, 1528), (1527, 1527), (1526, 1526), (1525, 1525), (1524, 1524), (1523, 1523), (1522, 1522), (1521, 1521), (1520, 1520), (1519, 1519), (1518, 1518), (1517, 1517), (1516, 1516), (1515, 1515), (1514, 1514), (1513, 1513), (1512, 1512), (1511, 1511), (1510, 1510), (1509, 1509), (1508, 1508), (1507, 1507), (1506, 1506), (1505, 1505), (1504, 1504), (1503, 1503), (1502, 1502), (1501, 1501), (1500, 1500)], verbose_name='год издания')),
                ('publisher', models.CharField(verbose_name='издательство', max_length=30)),
                ('description', ckeditor.fields.RichTextField(verbose_name='описание')),
                ('book_file', models.FileField(upload_to=library.models.UPLOAD_TO, verbose_name='книга')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(to='library.Category', verbose_name='категория', related_name='books'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(related_name='books', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
