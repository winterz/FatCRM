/*
  This file is part of FatCRM, a desktop application for SugarCRM written by KDAB.

  Copyright (C) 2015 Klarälvdalens Datakonsult AB, a KDAB Group company, info@kdab.com
  Authors: David Faure <david.faure@kdab.com>
           Michel Boyer de la Giroday <michel.giroday@kdab.com>
           Kevin Krammer <kevin.krammer@kdab.com>

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef NOTESDIALOG_H
#define NOTESDIALOG_H

#include <QDialog>
#include <QDateTime>

namespace Ui {
class NotesDialog;
}
class SugarEmail;
class SugarNote;

// internal. Generic representation for notes and emails, to sort them by date.
struct NoteText
{
    NoteText() {}
    NoteText(const QDateTime &dt, const QString &htmlHeader, const QString &text)
        : m_date(dt), m_htmlHeader(htmlHeader), m_text(text) {}

    bool operator<(const NoteText &other) const {
        // Most recent at the top
        return m_date > other.m_date;
    }

    QString text() const { return m_text; }
    QString htmlHeader() const { return m_htmlHeader; }
private:
    QDateTime m_date;
    QString m_htmlHeader;
    QString m_text;
};

class NotesDialog : public QDialog
{
    Q_OBJECT

public:
    explicit NotesDialog(QWidget *parent = 0);
    ~NotesDialog();

    void addNote(const SugarNote &note);
    void addEmail(const SugarEmail &email);

    void setVisible(bool visible) Q_DECL_OVERRIDE;

private:
    QVector<NoteText> m_notes;
    Ui::NotesDialog *ui;
};

#endif // NOTESDIALOG_H
