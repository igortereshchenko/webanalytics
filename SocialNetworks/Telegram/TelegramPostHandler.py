class TelegramPostHandler:
    @staticmethod
    def get_article_row(url=None, date=None, title=None, subtitle=None, html=None, text=None, translation=None):
        """
        Create article-dictionary representation

        :param id:
        :param author_id:
        :param date: publication datetime


        :param html: html
        :param text: cleared text

        :param translation_en: english translation


        :return: dictionary
        """
        return {
            # message_id
            # from
            # date
            # chat
            # forward_from
            # forward_from_chat
            # forward_from_message_id
            # forward_date
            # reply_to_message
            # text
            # entities
            # caption_entities
            # caption
            # contact
            # location

        }



    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        """
        Parse list of articles

        :param url_root: server url
        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: dictionary{
                             url_1:{
                                    "url": url_1,
                                    "date": date,
                                    "title": title,
                                    "subtitle": subtitle,
                                    "html": None,
                                    "text": None
                                    },
                             url_2:{
                                    ...
                                    }
                                    each row of dictionary could be created by  get_article_row method

        """
        return None

    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        """
        Parse article time

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :param day
        :param month
        :param hours
        :param minutes
        :param seconds
        :return: article datetime
        """

        return None

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):
        """
        Parse article subtitle

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: subtitle of article
        """

        return None

    @staticmethod
    def parse_article_text(html=None, soup=None):
        """
        Parse article text

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: html, cleaned html (without tag, text only)
        """

        return None, None


